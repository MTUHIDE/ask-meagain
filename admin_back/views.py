from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm


from .forms import QuestionForm, SurveyForm, UserCreationForm, CreateUserForm
from .models import Question, Choice, Survey, QuestionTypes


def index(request):
    context = {}
    return render(request, 'admin_back/index.html', context)


def registration(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_back:home')
    context = {'form': form}
    return render(request, 'admin_back/user_registration.html', context)

'''
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = Newusers()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.emailId = form.cleaned_data['emailId']
            user.password = form.cleaned_data['password']
            user.save()']

    context = {}
    return render(request, 'admin_back/user_registration.html', context)

'''
def dashboard(request):
    context = {}
    return render(request, 'admin_back/dashboard.html', context)

def loginauth(request):
    context = {}
    return render(request, 'admin_back/loginauth.html', context)

def forgotpass(request):
    context = {}
    return render(request, 'admin_back/forgot_password.html', context)

def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)

        if form.is_valid():
            survey = Survey()
            survey.title = form.cleaned_data['survey_name']

            survey.save()

            return redirect('admin_back:create_question', survey_id=survey.id)

    context = {}
    return render(request, 'admin_back/create_survey.html', context)

def manage_survey(request):
    context = {}
    return render(request, 'admin_back/manage_survey.html', context)

def manage_question(request, survey_id):
    info = Question.objects.all()
    survey = Choice.objects.get(id=survey_id)
    survey_name = survey.survey

    context = {'survey_name': survey_name,
               'question': survey,
               'detail': info}

    if request.method == 'POST':
        if 'add question' in request.POST:
            return redirect('admin_back:create_question', survey_id)
        elif 'delete' in request.POST:
            return redirect('admin_back:create_question', survey_id)

    return render(request, 'admin_back/manageQuestions.html', context)


def create_question(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    survey_name = survey.title
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            # submit question data to database
            question = Question()
            question.survey = survey
            question.text = form.cleaned_data['questiontext']

            # parses which question type was chosen
            qtype = form.cleaned_data['answertype']
            if qtype.__eq__('radio'):
                question.type = QuestionTypes.RADIO
            elif qtype.__eq__('checkbox'):
                question.type = QuestionTypes.CHECKBOX

            choice1 = Choice()
            choice1.survey = survey
            choice1.question = question
            choice1.text = form.cleaned_data['choice1text']

            choice2 = Choice()
            choice2.survey = survey
            choice2.question = question
            choice2.text = form.cleaned_data['choice2text']

            question.save()
            choice1.save()
            choice2.save()

    context = {'survey_name': survey_name}
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
def redirect_to_home(request):
    return HttpResponseRedirect('admin')

'''
def results(request):
   obj = Choice.objects.get(id=1)
   context = {
            'survey': obj.survey,
            'question': obj.question,
            'text': obj.text,
            'votes': obj.votes,
          }
   
   return render(request, 'admin_back/results.html', context)
'''
def results(request):
    Choice.objects.all()
    info = Choice.objects.all()
    print(info)
    resultdata = {'detail': info}
    print(resultdata)
    print(request)
    return render(request, 'admin_back/results.html', resultdata)