from datetime import datetime
from elasticsearch import Elasticsearch

import CompareImagepHash

es = Elasticsearch() #create a localhost server connection, or Elasticsearch("ip")


def insert():
    pass

def create():
    phash = CompareImagepHash.get_phash("1.jpg")
    es.create(index="pimage", doc_type="image",
              body={"path":"1.jpg", "phash": phash})

def add(body):
    es.index('pimage', 'image', body=body)

def detete():
    es.indices.delete("pimage")

def search(phash):
    body = {
        "query":{
            "term":{
                "phash": phash
            }
        }
    }
    data = es.search('pimage', 'image', body)
    print(data)
    return data

if __name__ == '__main__':
    # detete()
    # create()
    # phash = CompareImagepHash.get_phash("1.jpg")
    # body = {"path": "1.jpg", "phash": phash}
    # add(body)

    phash = CompareImagepHash.get_phash("1.jpg")
    search('1100011111000011110000111110011111110111111101111110001111100111')
