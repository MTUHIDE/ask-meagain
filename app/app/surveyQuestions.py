from flask_wtf import Form
from wtforms import StringField, SubmitField


class QuestionForm(Form):
    question = StringField("Question 1")
    answer1 = SubmitField("Answer 1")
    answer2 = SubmitField("Answer 2")
    answer3 = SubmitField("Answer 3")
    answer4 = SubmitField("Answer 4")

