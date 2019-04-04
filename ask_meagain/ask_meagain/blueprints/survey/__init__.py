from flask import Blueprint,render_template,request, flash
from ask_meagain.surveyQuestions import QuestionForm
survey = Blueprint('survey',__name__,template_folder='templates')

@survey.route("/SurveyLandingPage/")
def surveyLandingPage():
    return render_template('surveyLanding.html')


@survey.route("/ThankYouPage/")
def thankYouPage():
    return render_template('thankYou.html')

@survey.route("/survey", methods=['GET', 'POST'])
def surveyQuestion():
    form = QuestionForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('ERR')
            return render_template('survey.html', form = form)
        else:
            return render_template('thankYou.html')
    elif request.method == 'GET':
        return render_template('survey.html', form = form)

