from flask import Blueprint,render_template,request, flash, redirect, url_for
from ask_meagain.blueprints.survey.surveyQuestions import QuestionForm
survey = Blueprint('survey',__name__,template_folder='templates')

@survey.route("/")
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
            return redirect(url_for('survey.thankYouPage'))
    elif request.method == 'GET':
        return render_template('survey.html', form = form)
