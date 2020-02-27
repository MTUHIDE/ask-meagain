from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    #template = loader.get_template('admin/index.html')
    context = {}
    return render(request, 'admin_back/index.html', context)

def loginauth(request):
    context = {}
    return render(request, 'admin_back/loginauth.html', context)


def create_question(request, survey_id):
    context = {}
    template = loader.get_template('admin_back/create_question.html')
    return HttpResponse(template.render(context, request))

def home(request):
    context = {}
    template = loader.get_template('admin_back/home.html')
    return render(request, 'admin_back/home.html', context)


