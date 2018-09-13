from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('SearchImage')

def search(name, all_orientations=False):
    es = Elasticsearch()
    ses = SignatureES(es, size=15)
    logger.info("Search image %s...", name)
    #result = ses.search_image(name)
    result = ses.search_image(name, all_orientations)
    size = len(result)
    if size == 0:
        logger.info("No image found for %s", name)
        distance_cutoff=0.6
        ses = SignatureES(es, size=15, distance_cutoff=distance_cutoff)
        result = ses.search_image(name, all_orientations)
        logger.info("Second distance_cutoff %s found %s image for %s", distance_cutoff, size, name)
    else:
        logger.info("%s images found for %s", size, name)
    #result = ses.search_single_record(name)
    return result

