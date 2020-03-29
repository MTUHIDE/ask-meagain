from django.contrib import admin
from django.urls import include, path
from admin_back import views
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from social_core.utils import setting_name

extra = getattr(settings,setting_name('TRAILING_SLASH'), True) and '/' or ''

app_name = 'social'

urlpatterns = [
    #url(r'^login /(?P<backend>[^/]+){0}$'.format(extra), views.auth, name='begin'),
    #url(r'^complete/(?P<backend>[^/]+){0}$'.format(extra), views.complete, name='complete'),
    #url(r'^disconnect/(?P<backend>[^/]+){0}$'.format(extra), views.disconnect, name='disconnect'),
    #url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+){0}$'.format(extra), views.disconnect, name='disconnect_individual'),
    # url(r'^',include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('', views.home, name='home'),
    path('admin/', include('admin_back.urls')),
    path('polls/', include('polls.urls')),

]
