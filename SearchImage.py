from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('SearchImage')

def search(name):
    es = Elasticsearch()
    ses = SignatureES(es)
    logger.info("Search image %s...", name)
    result = ses.search_image(name)
    return result

#search('images/001.jpg')