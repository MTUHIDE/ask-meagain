from flask import Blueprint,render_template
from ask_meagain.models import TestResponses, TestChoices, TestQuestions

admin = Blueprint('admin',__name__,template_folder='templates')

@admin.route("/alterQuestion/")
def alterQuestion():
    return render_template('alterQuestion.html')

@admin.route("/ResultsPage/")
def resultsPage():
    questions = TestQuestions.query.filter_by(active=True).all();
    return render_template('ResultsPage.html', questions = questions)

@admin.route("/QuestionResultsPage/<id>")
def questionResultPage(id):
    data = TestResponses.query.filter_by(qid = id).first() 
    return render_template('questionResults.html')

@admin.route("/questionData/<id>")
def questionData(id):
    data = TestResponses.query.filter_by(qid = id).all()
    return jsonify(data)
