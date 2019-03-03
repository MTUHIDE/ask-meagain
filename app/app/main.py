from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.surveyQuestions import QuestionForm

app = Flask(__name__)
app.secret_key = "dev_key"
Bootstrap(app)

# Defines our database connections
app.config['SQLALCHEMY_BINDS'] = {
    'testQ':    'sqlite:////app/dbFiles/testing.db',
    'testC':    'sqlite:////app/dbFiles/testing.db',
    'testR':    'sqlite:////app/dbFiles/testing.db'
    # Add db files in the format above for actually holding production data
    }
db = SQLAlchemy(app)

# Creates our schema
# Sqlite3 only supports one schema per db
# The three test classes are for tables in one schema
# schema may be moved away from this file later - Max S.
class TestQuestions(db.Model):
    __bind_key__ = 'testQ'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionText = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
    choices = db.relationship('TestChoices', backref='testQ')
    responces = db.relationship('TestResponses', backref='testR')

class TestChoices(db.Model):
    __bind_key__ = 'testC'
    qid = db.Column(db.Integer, db.ForeignKey('test_questions.id'))
    choiceText = db.Column(db.Text)
    choiceId = db.Column(db.Integer, primary_key=True, autoincrement=True)

class TestResponses(db.Model):
    __bind_key__ = 'testR'
    resId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qid = db.Column(db.Integer, db.ForeignKey('test_questions.id'))
    responce = db.Column(db.Integer)
    dt = db.Column(db.DateTime)
    studentId = db.Column(db.Integer)

# Creates db & schema. Queries now ready to be made
db.create_all()

@app.route("/")
def hello():
    return render_template('survey.html')


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
    return render_template('ResultsPage.html')


@app.route("/SurveyLandingPage/")
def surveyLandingPage():
    return render_template('SurveyLandingPage.html')


@app.route("/ThankYouPage/")
def thankYouPage():
    return render_template('ThankYouPage.html')

@app.route("/survey", methods=['GET', 'POST'])
def surveyQuestion():
    form = QuestionForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('ERR')
            return render_template('survey.html', form = form)
        else:
            return render_template('ThankYouPage.html')
    elif request.method == 'GET':
        return render_template('survey.html', form = form)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='127.0.0.1', debug=True, port=80)
