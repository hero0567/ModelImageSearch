"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.static import serve

from web.settings import BASE_DIR
from web.view import home
from web.view import upload
from web.view import download

# Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join('templates/static')
# STATICFILES_DIRS = [
#     ("css", os.path.join(STATIC_ROOT, 'css')),
#     ("img", os.path.join(STATIC_ROOT, 'img')),
#     ("js", os.path.join(STATIC_ROOT, 'js')),
# ]

urlpatterns = [
    path('', home.hello),
    path('admin/', home.admin),
    path('login/', admin.site.urls),
    path('search/', home.view),
    path('delete/', home.delete),
    path('add/', home.add),
    path('reload/', home.reload),
    path('vnotice/', home.vnotice),
    path('unotice/', home.unotice),
    path('upload/', upload.upload),
    path('download/', download.download),
]
