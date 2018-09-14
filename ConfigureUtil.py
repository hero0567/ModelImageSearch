import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('ConfigureUtil')

notice = ""


def read_notice():
    global notice
    return notice


def load_notice():
    global notice
    with open('configure.text', encoding='UTF-8') as file:
        for line in file:
            if line.startswith('notice='):
                notice = line.replace('notice=', '')
                logger.info("Read notice %s", notice)
                return notice


def write_notice(new_notice):
    global notice
    file='configure.text'
    notice_key='notice='
    file_data = ""
    notiece_existed = False
    logger.info("Update notice %s", new_notice)
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(notice_key):
                line = notice_key + new_notice
                notiece_existed = True
            file_data += line
        if not notiece_existed:
            file_data += '\r\n' + notice_key + new_notice
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)
    notice=new_notice
    logger.info("Update successful.")

