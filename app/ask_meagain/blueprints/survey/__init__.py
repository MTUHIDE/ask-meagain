from flask import Blueprint,render_template,request, flash, redirect, url_for
from ask_meagain.blueprints.survey.surveyQuestions import QuestionForm
from ask_meagain.models import TestQuestions
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
            print(request.form)
            return redirect(url_for('survey.thankYouPage'))
    elif request.method == 'GET':
        question = TestQuestions.query.order_by(TestQuestions.id.desc()).first()
        form.question.default = question.questionText
        form.answer1.label.text = question.choices[0].choiceText 
        form.answer2.label.text = question.choices[1].choiceText 
        form.answer3.label.text = question.choices[2].choiceText 
        form.answer4.label.text = question.choices[3].choiceText 
        return render_template('survey.html', form = form)
