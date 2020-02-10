from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', include('admin_back.urls')),
    path('polls/', include('polls.urls'))
]