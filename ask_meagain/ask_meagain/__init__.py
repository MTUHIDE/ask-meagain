from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from ask_meagain.surveyQuestions import QuestionForm
from flask import jsonify

app = Flask(__name__)
app.secret_key = "dev_key"
Bootstrap(app)

# Defines our database connections
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////app/dbFiles/testing.db'
db = SQLAlchemy(app)

# Creates our schema
# Sqlite3 only supports one schema per db
# The three test classes are for tables in one schema
from ask_meagain.models import TestResponses, TestChoices, TestQuestions

# Creates db & schema. Queries now ready to be made
db.create_all()

@app.route("/")
def hello():
    return render_template('menu.html')


@app.errorhandler(500)
@app.errorhandler(404)
def errorPage(error):
    return render_template('error.html', error=error)


@app.route("/menu/")
def menu():
    return render_template('menu.html')

@app.route("/alterQuestion/")
def alterQuestion():
    return render_template('alterQuestion.html')

@app.route("/ResultsPage/")
def resultsPage():
    questions = TestQuestions.query.filter_by(active=True).all();
    return render_template('ResultsPage.html', questions = questions)

@app.route("/QuestionResultsPage/<id>")
def questionResultPage(id):
    data = TestResponses.query.filter_by(qid = id).first() 
    return render_template('questionResults.html')

@app.route("/questionData/<id>")
def questionData(id):
    data = TestResponses.query.filter_by(qid = id).all()
    return jsonify(data)

@app.route("/SurveyLandingPage/")
def surveyLandingPage():
    return render_template('surveyLanding.html')


@app.route("/ThankYouPage/")
def thankYouPage():
    return render_template('thankYou.html')

@app.route("/survey", methods=['GET', 'POST'])
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


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='127.0.0.1', debug=True, port=80)
