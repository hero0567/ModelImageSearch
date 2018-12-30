import os
from django.http import StreamingHttpResponse#文件流

def download(request):
    zipPath = request.GET.get('file')
    zipName = zipPath.split(os.path.sep)[-1]
    response = StreamingHttpResponse(file_read(zipPath))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(zipName)
    return response

def file_read(file_name, chunk_size=2048):
    with open(file_name,'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
