from django.urls import path
from admin_back import views


app_name = 'admin_back'

urlpatterns = [
    path('login/', views.loginauth, name='loginauth'),
    path('', views.home, name='home'),
    path('create_question/<int:survey_id>/', views.create_question, name='create_question'),
    path('create_survey/', views.create_survey, name='create_survey'),
    path('form_test', views.form_test, name='form_test'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage_survey/', views.manage_survey, name='manage_survey'),
    path('manage_question/<int:survey_id>/', views.manage_question, name='manage_question'),
    path('registration/', views.registration, name='user_registration'),
    path('results/', views.results, name='results'),
    path('forgot_password/', views.forgotpass, name='forgot_password'),

]