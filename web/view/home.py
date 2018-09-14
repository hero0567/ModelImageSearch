from django.shortcuts import render
import logging.config
import DeleteImage
import AddImage
import datetime
import ConfigureUtil

logging.config.fileConfig('log.conf')
logger = logging.getLogger('home')

def hello(request):
    logger.info("Loading home page.")
    return render(request, 'home.html', None)


def admin(request):
    logger.info("Loading admin page.")
    pwd = request.GET.get('pwd')
    if "123" == pwd:
        return render(request, 'admin.html', None)
    return render(request, 'admin.html', None)

def view(request):
    logger.info("Loading view page.")
    context = {}
    context['notice'] = ConfigureUtil.read_notice()
    return render(request, 'search.html', context)

def delete(request):
    logger.info("Loading delete page.")
    starttime = datetime.datetime.now()
    DeleteImage.delete()
    endtime = datetime.datetime.now()
    addtime = (endtime-starttime).seconds
    context = {}
    context['addtime'] = addtime
    return render(request, 'success.html', context)

def add(request):
    logger.info("Loading add page.")
    starttime = datetime.datetime.now()
    AddImage.import_image("images")
    endtime = datetime.datetime.now()
    addtime = (endtime-starttime).seconds
    context = {}
    context['addtime'] = addtime
    return render(request, 'success.html', context)

def vnotice(request):
    logger.info("Loading vnotice page.")
    return render(request, 'notice.html', None)

def unotice(request):
    logger.info("Loading unotice page.")
    notice = request.POST.get('notice')
    ConfigureUtil.write_notice(notice)
    return render(request, 'success.html', None)