from django.contrib import admin
from django.urls import include, path
from admin_back import views
from django.urls import path, include

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', views.home, name='home'),
    path('admin/', include('admin_back.urls')),
    path('polls/', include('polls.urls')),

]
