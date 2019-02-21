from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Defines our database connections
app.config['SQLALCHEMY_BINDS'] = {
    'testing':    'sqlite:////app/dbFiles/testing.db',
    # Add db files in the format above for actually holding production data
    }
db = SQLAlchemy(app)

# Creates our schema
# Sqlite3 only supports one schema per db
class Testdata(db.Model):
    __bind_key__ = 'testing'
    id = db.Column(db.Integer, primary_key=True)
    sampleStr = db.Column(db.String(80))
    sampleNum = db.Column(db.Float)

# Creates db & schema. Queries now ready to be made
db.create_all()

@app.route("/")
def hello():
    return "Hello World from HIDE's new solution"


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

@app.route("/surveyQuestion/")
def surveyQuestion():
    return render_template('surveyQuestion.html')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='127.0.0.1', debug=True, port=80)
