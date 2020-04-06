from django.urls import path
from admin_back import views


app_name = 'admin_back'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginauth, name='loginauth'),
    path('home/', views.home, name='home'),
    path('create_question/<int:survey_id>/', views.create_question, name='create_question'),
    path('form_test', views.form_test, name='form_test'),
    path('dashboard/', views.dashboard, name='dashboard'),
]