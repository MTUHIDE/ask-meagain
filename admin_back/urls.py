from django.urls import path

from . import views

app_name = 'admin_back'

urlpatterns = [
    path('', views.index, name='index'),
]