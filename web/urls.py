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
from django.contrib import admin
from django.urls import path
from web.view import home
from web.view import upload

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


    #path('static/','django.views.static.serve',{'document_root':settings.STATIC_ROOT}, name='static'),
    #path('uploadimage/', 'django.views.static.serve', {'document_root':'C:\\workspace\\ModelImageSearch\\uploadimage'}),
]
