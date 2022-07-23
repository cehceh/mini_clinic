"""metclinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from os import name
from .utils import backup
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
import debug_toolbar

from .utils import talk_with_reg
from apps.home.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontpage 
    path('', frontpage, name='frontpage'),

    path('backup/', backup, name='backup'),
    
    #
    path('lab/', include('apps.labs.urls', namespace='labs')),
    path('patientdata/', include('apps.patientdata.urls', namespace='patientdata')),
    path('pasthistory/', include('apps.pasthistory.urls', namespace='pasthistory')),
    path('presenthistory/', include('apps.presenthistory.urls', namespace='presenthistory')),

    path('revisitdrug/', include('apps.revisitdrug.urls', namespace='revisitdrug')),
    path('revisits/', include('apps.revisits.urls', namespace='revisits')),
    
    path('search/', include('apps.search.urls', namespace='search')),
    
    path('reports/', include('apps.reports.urls', namespace='reports')),
    path('visits/', include('apps.visits.urls', namespace='visits')),
    path('medicine/', include('apps.visitdrug.urls', namespace='visitdrug')),

    path('any/', talk_with_reg, name='talk_with_reg'),
    path('__debug__/', include(debug_toolbar.urls)),


    # the next two linesare for (DEBUG=False) to static works without any problem
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
