from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import os.path
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('AddImage')

es = Elasticsearch()
ses = SignatureES(es)
count = 0

def add_dir_image(src):
    global count
    logger.info('Try to add images from %s', src)
    if os.path.isdir(src):
        files = os.listdir(src)
        for file in files:
            if os.path.isdir(os.path.join(src, file)):
                add_dir_image(os.path.join(src, file))
                continue
            else:
                if file.endswith(".jpg"):
                    ses.add_image(os.path.join(src, file))
                    count=count+1


def import_image(src):
    add_dir_image(src)
    logger.info("Total %s images added to server.", count)

if __name__ == '__main__':
    import_image(os.path.join("images"))

