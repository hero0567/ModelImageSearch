from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import os.path
import logging.config
import sys

logging.config.fileConfig('log.conf')
logger = logging.getLogger('AddImage')

es = Elasticsearch()
ses = SignatureES(es)
count = 0
error = 0
existed = 0
skipCount = 0
skip = False
list = []

def add_dir_image(src, lastImg=None):
    global count
    global error
    global skip
    global existed
    global skipCount
    logger.info('Try to add images from %s', src)
    if os.path.isdir(src):
        files = os.listdir(src)
        for file in files:
            if os.path.isdir(os.path.join(src, file)):
                add_dir_image(os.path.join(src, file), lastImg)
                continue
            else:
                if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
                    if skip and lastImg != None and os.path.join(src, file) != lastImg:
                        logger.info("Skip image %s", os.path.join(src, file))
                        skipCount = skipCount + 1
                        continue
                    skip = False                    
                    if check_exist_and_insert(os.path.join(src, file)):
                        logger.info("Existed image %s", os.path.join(src, file))
                        existed = existed + 1
                        continue
                    logger.info("Add image %s", os.path.join(src, file))    
                    try:
                        ses.add_image(os.path.join(src, file))
                    except:
                        error = error + 1
                        logger.error("Failed to add %s to server", os.path.join(src, file))
                    count=count+1
                    
def check_exist_and_insert(file):
    if file not in list:
        fp=open("list","a",encoding="utf-8")
        fp.write(file+"\n")
        return False
    return True 
    
def load_image_list():
    with open('list', encoding='UTF-8') as file:
        for id in file:
            id = id.replace("\n", "")
            list.append(id)
    logger.info("Total %s id load from disk.", len(list))

def import_image(src, lastImg):
    try:
        global count
        global error
        global skip
        global existed
        global skipCount
        count = 0
        error = 0
        existed = 0
        skipCount = 0
        load_image_list()
        if lastImg != None:
            skip = True
        add_dir_image(src, lastImg)
    except Exception as e:
        logger.error("Failed to added images.")
        logger.error(e)
    logger.info("Total %s skip images.", skipCount)
    logger.info("Total %s existed images.", existed)
    logger.info("Total %s images added to server.", count)
    logger.info("Total %s error images add failed to server.", error)

if __name__ == '__main__':
    lastImg = None
    if(len(sys.argv) == 2):
        lastImg = sys.argv[1]
    import_image(os.path.join("images"), lastImg)

