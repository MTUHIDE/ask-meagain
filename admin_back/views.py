from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .forms import QuestionForm
from .models import Question, Choice, QuestionTypes, Survey


def index(request):
    context = {}
    return render(request, 'admin_back/index.html', context)


def loginauth(request):
    context = {}
    return render(request, 'admin_back/loginauth.html', context)


def create_question(request, survey_id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            # submit question data to database
            question = Question()
            question.survey = Survey.objects.get(id=survey_id)
            question.text = form.cleaned_data['questiontext']
            # THIS IS HARD CODED FOR NOW
            question.type = QuestionTypes.RADIO

            choice1 = Choice()
            choice1.survey = Survey.objects.get(id=survey_id)
            choice1.question = question
            choice1.text = form.cleaned_data['choice1text']

            choice2 = Choice()
            choice2.survey = Survey.objects.get(id=survey_id)
            choice2.question = question
            choice2.text = form.cleaned_data['choice2text']

            question.save()
            choice1.save()
            choice2.save()

    context = {'survey_id': survey_id}
    template = loader.get_template('admin_back/create_question.html')
    return HttpResponse(template.render(context, request))


def home(request):
    context = {}
    return render(request, 'admin_back/home.html', context)


def form_test(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            # data is processed here
            return HttpResponseRedirect('/')

    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'admin_back/form_test.html', context)
