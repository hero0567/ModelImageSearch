
import os
from django.http import HttpResponse
from django.shortcuts import render
import SearchImage
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('upload')

def upload(request):
    logger.info("Send upload request.")
    if request.method == 'POST':# 获取对象
        file = request.FILES.get('image_data')
        logger.info("upload %s to search", file.name)
        f = open(os.path.join('uploadimage', file.name), 'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()

    context = {}
    result = SearchImage.search(os.path.join('uploadimage', file.name))
    context['load_img'] = os.path.join('/static', 'uploadimage', file.name)
    context['result'] = result
    return render(request, 'search_result.html', context)
    #return render(request, 'upload/upload.html')