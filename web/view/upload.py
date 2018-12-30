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
        loadZip(sr)
        load_img = os.path.join('/static', 'uploadimage', file.name)
        result["key"] = load_img;
        result["value"] = sr;
        results.append(result)
    endtime = datetime.datetime.now()
    searchtime = (endtime - starttime).seconds
    context['searchtime'] = searchtime
    context['results'] = results
    return render(request, 'search_result.html', context)


def loadZip(sr):
    for result in sr:
        project = getProject(result['path'])
        zip_path = ''
        if project == 1:  # amazon
            zip_path = loadAmazonZip(result['path'])
        elif project == 2:  # amazon_old
            zip_path = loadAmazonOldZip(result['path'])
        elif project == 3:  # houzz
            zip_path = loadHouzzZip(result['path'])
        else:
            logger.warning("No project found for %s", result['path'])
        result['zip_path'] = zip_path


def getProject(imgPath):
    amazon_path = "images" + os.path.sep + "Reference images" + os.path.sep + "Amazon"
    amazon_old_path = "images" + os.path.sep + "Reference images" + os.path.sep + "Amazon_old"
    houzz_path = "images" + os.path.sep + "Reference images" + os.path.sep + "Houzz"
    if imgPath.startswith(amazon_old_path):
        logger.info("find %s project %s", imgPath, "Amazon Old")
        return 2;
    if imgPath.startswith(amazon_path):
        logger.info("find %s project %s", imgPath, "Amazon")
        return 1;
    if imgPath.startswith(houzz_path):
        logger.info("find %s project %s", imgPath, "Houzz")
        return 3;
    return 0


def loadAmazonZip(imgPath):
    # 父文件夹的名字
    # return imgPath.split(os.path.sep)[-2]
    return ''


def loadAmazonOldZip(imgPath):
    # 图片的名字
    imageName = imgPath.split(os.path.sep)[-1]
    dotIndex = imageName.find(".");
    zipName = imageName
    if dotIndex > -1:
        zipName = imageName[0:dotIndex]

    zipPath = os.path.join('images', 'ZIP', 'Amazon', zipName + ".zip")
    if not os.path.exists(zipPath):
        zipPath = ''
    return zipPath


def loadHouzzZip(imgPath):
    # 父文件夹的名字中下滑线后面的数字
    # eg：RO1000_34091934
    imageName = imgPath.split(os.path.sep)[-2]
    zipName = imageName.split("_")[-1]

    zipPath = os.path.join('images', 'ZIP', 'Houzz', zipName + ".zip")
    if not os.path.exists(zipPath):
        zipPath = ''
    return zipPath
