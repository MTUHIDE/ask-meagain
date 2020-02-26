from django.urls import path
from admin_back import views


app_name = 'admin_back'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginauth, name='loginauth'),
    path('create_question/<int:survey_id>/', views.create_question, name='create_question'),

]