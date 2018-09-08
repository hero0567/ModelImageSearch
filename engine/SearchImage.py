from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

def search(name):
    es = Elasticsearch()
    ses = SignatureES(es)

    result = ses.search_image(name)
    print(result)
    return result

#search('images/001.jpg')