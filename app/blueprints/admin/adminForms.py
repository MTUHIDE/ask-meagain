from flask_wtf import FlaskForm
from wtforms import StringField

class newQuestionForm(FlaskForm):
    question = StringField('Question')
    optionOne = StringField('optionOne')
    optionTwo= StringField('optionTwo')
    optionThree = StringField('optionThree')
    optionFour = StringField('optionFour')
