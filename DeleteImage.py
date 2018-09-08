from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('DeleteImage')

es = Elasticsearch()
ses = SignatureES(es)

def delete():
    es.indices.delete("images")
