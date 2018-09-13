from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('DeleteImage')

def delete():
    es = Elasticsearch()
    ses = SignatureES(es)
    es.indices.delete("images")
