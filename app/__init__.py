from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.surveyQuestions import QuestionForm
from flask import jsonify

app = Flask(__name__)
app.secret_key = "dev_key"
Bootstrap(app)

# Defines our database connections
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../dbFiles/testing.db'
db = SQLAlchemy(app)

# Creates our schema
# Sqlite3 only supports one schema per db
# The three test classes are for tables in one schema
from app.models import TestResponses, TestChoices, TestQuestions
from app.blueprints.survey import survey
from app.blueprints.admin import admin

app.register_blueprint(survey,url_prefix='/survey')
app.register_blueprint(admin,url_prefix='/admin')
# Creates db & schema. Queries now ready to be made
db.create_all()

@app.route("/")
def index():
    return render_template('menu.html')


@app.errorhandler(500)
@app.errorhandler(404)
def errorPage(error):
    return render_template('error.html', error=error)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='127.0.0.1', debug=True, port=80)
