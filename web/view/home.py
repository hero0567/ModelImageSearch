from django.shortcuts import render
import logging.config
import DeleteImage
import AddImage

logging.config.fileConfig('log.conf')
logger = logging.getLogger('home')

def hello(request):
    logger.info("Loading home page.")
    return render(request, 'home.html', None)


def admin(request):
    logger.info("Loading admin page.")
    return render(request, 'admin.html', None)

def view(request):
    return render(request, 'search.html', None)

def delete(request):
    DeleteImage.delete()
    return render(request, 'success.html', None)

def add(request):
    AddImage.import_image("images")
    return render(request, 'success.html', None)