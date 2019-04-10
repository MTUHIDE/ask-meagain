from flask import Blueprint,render_template,request
from ask_meagain.models import TestResponses, TestChoices, TestQuestions
from ask_meagain.blueprints.admin.adminForms import newQuestionForm
from ask_meagain import db

admin = Blueprint('admin',__name__,template_folder='templates')

@admin.route("/alterQuestion/")
def alterQuestion():
    questions = TestQuestions.query.filter_by(active = True).all()
    return render_template('alterQuestion.html',questions = questions)

@admin.route("/createQuestion/",methods=['GET','POST'])
def createQuestion():
    form = newQuestionForm()
    if(request.method == 'POST'):
        question = TestQuestions()
        question.questionText = request.form['question'] 
        db.session.add(question)
        db.session.commit()

        
        optionOne = TestChoices(qid=question.id,choiceText=request.form['optionOne'])
        optionTwo = TestChoices(qid=question.id,choiceText=request.form['optionTwo'])
        optionThree = TestChoices(qid=question.id,choiceText=request.form['optionThree'])
        optionFour = TestChoices(qid=question.id,choiceText=request.form['optionFour'])

        db.session.add(optionOne)
        db.session.add(optionTwo)
        db.session.add(optionThree)
        db.session.add(optionFour)
        db.session.commit()
    return render_template("create.html",form=form)

@admin.route("/ResultsPage/")
def resultsPage():
    questions = TestQuestions.query.filter_by(active=True).all();
    return render_template('ResultsPage.html', questions = questions)

@admin.route("/QuestionResultsPage/<id>")
def questionResultPage(id):
    data = TestQuestions.query.filter_by(id = id).first() 
    return render_template('questionResults.html',question = data)

@admin.route("/questionData/<id>")
def questionData(id):
    data = TestResponses.query.filter_by(qid = id).all()
    printf(jsonify(data))
    return jsonify(data)
