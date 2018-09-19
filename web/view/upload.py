
import os
from django.http import HttpResponse
from django.shortcuts import render
import SearchImage
import logging.config
import datetime

logging.config.fileConfig('log.conf')
logger = logging.getLogger('upload')

def upload(request):
    logger.info("Send upload request.")

    starttime = datetime.datetime.now()
    files = request.FILES.getlist('image_data')
    image_match = request.POST.get('image_match')
    print(type(image_match))
    print("111")
    orientations = False
    context = {}
    results = []

    for file in files:
        result = {}
        logger.info("upload %s to search", file.name)
        f = open(os.path.join('uploadimage', file.name), 'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()


        all_orientations = request.POST.get('all_orientations')
        if "true" == all_orientations:
            orientations = True
        sr = SearchImage.search(os.path.join('uploadimage', file.name), orientations, image_match)
        load_img = os.path.join('/static', 'uploadimage', file.name)
        result["key"] = load_img;
        result["value"] = sr;
        results.append(result)
    endtime = datetime.datetime.now()
    searchtime = (endtime-starttime).seconds
    context['searchtime'] = searchtime
    context['results'] = results
    return render(request, 'search_result.html', context)
