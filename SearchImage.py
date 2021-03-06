from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('SearchImage')

def search(name, all_orientations=False, image_match=0.6):
    es = Elasticsearch()
    ses = SignatureES(es, size=15, timeout='30s')
    logger.info("Search image %s...", name)
    #result = ses.search_image(name)
    result = ses.search_image(name, all_orientations)
    size = len(result)
    if size == 0 and image_match != None:
        logger.info("No image found for %s", name)
        ses = SignatureES(es, size=15, timeout='30s', distance_cutoff=float(image_match))
        result = ses.search_image(name, all_orientations)
        logger.info("Second distance_cutoff %s found %s image for %s", image_match, size, name)
    else:
        logger.info("%s images found for %s", size, name)
    #logger.info("%s images found for %s", size, name)
    #result = ses.search_single_record(name)
    return result

