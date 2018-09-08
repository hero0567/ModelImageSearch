from django.shortcuts import render
import logging.config
import DeleteImage
import AddImage
import datetime

logging.config.fileConfig('log.conf')
logger = logging.getLogger('home')

def hello(request):
    logger.info("Loading home page.")
    return render(request, 'home.html', None)


def admin(request):
    pwd = request.GET.get('pwd')
    if "123" == pwd:
        return render(request, 'admin.html', None)
    return render(request, 'admin.html', None)

def view(request):
    return render(request, 'search.html', None)

def delete(request):
    starttime = datetime.datetime.now()
    DeleteImage.delete()
    endtime = datetime.datetime.now()
    addtime = (endtime-starttime).seconds
    context = {}
    context['addtime'] = addtime
    return render(request, 'success.html', context)

def add(request):
    starttime = datetime.datetime.now()
    AddImage.import_image("images")
    endtime = datetime.datetime.now()
    addtime = (endtime-starttime).seconds
    context = {}
    context['addtime'] = addtime
    return render(request, 'success.html', context)