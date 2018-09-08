from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import os.path
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('AddImage')

es = Elasticsearch()
ses = SignatureES(es)

def add_dir_image(src):
    logger.info('Try to add images from %s', src)
    if os.path.isdir(src):
        files = os.listdir(src)
        for file in files:
            if os.path.isdir(os.path.join(src, file)):
                add_dir_image(os.path.join(src, file))
                continue
            else:
                ses.add_image(os.path.join(src, file))

if __name__ == '__main__':
    add_dir_image(os.path.join("images"))

