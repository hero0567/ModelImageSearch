from django.shortcuts import render
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('home')

def hello(request):
    logger.info("Loading home page.")
    return render(request, 'home.html', None)