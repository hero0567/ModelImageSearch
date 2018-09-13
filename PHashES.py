from datetime import datetime
import numpy as np
from collections import deque

from image_match.signature_database_base import SignatureDatabaseBase


class PHashES(SignatureDatabaseBase):
    """Elasticsearch driver for image-match

    """

    def __init__(self, es, index='pimages', doc_type='image', timeout='10s', size=15):
        """Extra setup for Elasticsearch

        Args:
            es (elasticsearch): an instance of the elasticsearch python driver
            index (Optional[string]): a name for the Elasticsearch index (default 'images')
            doc_type (Optional[string]): a name for the document time (default 'image')
            timeout (Optional[int]): how long to wait on an Elasticsearch query, in seconds (default 10)
            size (Optional[int]): maximum number of Elasticsearch results (default 100)
            *args (Optional): Variable length argument list to pass to base constructor
            **kwargs (Optional): Arbitrary keyword arguments to pass to base constructor

        Examples:
            >>> from elasticsearch import Elasticsearch
            >>> from image_match.elasticsearch_driver import SignatureES
            >>> es = Elasticsearch()
            >>> ses = SignatureES(es)
            >>> ses.add_image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
            >>> ses.search_image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
            [
             {'dist': 0.0,
              'id': u'AVM37nMg0osmmAxpPvx6',
              'path': u'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg',
              'score': 0.28797293}
            ]

        """
        self.es = es
        self.index = index
        self.doc_type = doc_type
        self.timeout = timeout
        self.size = size

    def search_single_record(self, rec):
        path = rec.pop('path')
        signature = rec.pop('signature')
        if 'metadata' in rec:
            rec.pop('metadata')

        # build the 'should' list
        should = [{'term': {word: rec[word]}} for word in rec]
        res = self.es.search(index=self.index,
                             doc_type=self.doc_type,
                             body={'query': {
                                 'bool': {'should': should}
                             },
                                 '_source': {'excludes': ['simple_word_*']}
                             },
                             size=self.size,
                             timeout=self.timeout)['hits']['hits']

        sigs = np.array([x['_source']['signature'] for x in res])

        if sigs.size == 0:
            return []

        dists = normalized_distance(sigs, np.array(signature))

        formatted_res = [{'id': x['_id'],
                          'score': x['_score'],
                          'metadata': x['_source'].get('metadata'),
                          'path': x['_source'].get('url', x['_source'].get('path'))}
                         for x in res]

        for i, row in enumerate(formatted_res):
            row['dist'] = dists[i]
        formatted_res = filter(lambda y: y['dist'] < self.distance_cutoff, formatted_res)

        return formatted_res

    def insert_single_record(self, rec, refresh_after=False):
        rec['timestamp'] = datetime.now()
        self.es.index(index=self.index, doc_type=self.doc_type, body=rec, refresh=refresh_after)

    def add_image(self, path, img=None, bytestream=False, metadata=None, refresh_after=False):
        """Add a single image to the database

        Args:
            path (string): path or identifier for image. If img=None, then path is assumed to be
                a URL or filesystem path
            img (Optional[string]): usually raw image data. In this case, path will still be stored, but
                a signature will be generated from data in img. If bytestream is False, but img is
                not None, then img is assumed to be the URL or filesystem path. Thus, you can store
                image records with a different 'path' than the actual image location (default None)
            bytestream (Optional[boolean]): will the image be passed as raw bytes?
                That is, is the 'path_or_image' argument an in-memory image? If img is None but, this
                argument will be ignored.  If img is not None, and bytestream is False, then the behavior
                is as described in the explanation for the img argument
                (default False)
            metadata (Optional): any other information you want to include, can be nested (default None)

        """
        rec = make_record(path, self.gis, self.k, self.N, img=img, bytestream=bytestream, metadata=metadata)
        self.insert_single_record(rec, refresh_after=refresh_after)

    def delete_duplicates(self, path):
        """Delete all but one entries in elasticsearch whose `path` value is equivalent to that of path.
        Args:
            path (string): path value to compare to those in the elastic search
        """
        matching_paths = [item['_id'] for item in
                          self.es.search(body={'query':
                                                   {'match':
                                                        {'path': path}
                                                    }
                                               },
                                         index=self.index)['hits']['hits']
                          if item['_source']['path'] == path]
        if len(matching_paths) > 0:
            for id_tag in matching_paths[1:]:
                self.es.delete(index=self.index, doc_type=self.doc_type, id=id_tag)
