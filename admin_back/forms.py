from django import forms

"""
    Creating a question requires an existing survey, to add one to your database do the following:
    In your terminal run 'python manage.py shell'
    
    >>> from admin_back.models import Survey, Question, Choice
    >>> survey = Survey(title="testSurvey")
    >>> survey.save()
"""

"""
    IMPORTANT
    Variable names in forms must match the names given in the HTML code, i.e.
    questiontext is the same variable name as the <input> tag in the HTML code has in its name element
"""


class QuestionForm(forms.Form):
    questiontext = forms.CharField(label='Question text', max_length=200)

    choice1text = forms.CharField(label='Choice 1', max_length=100)
    choice2text = forms.CharField(label='Choice 2', max_length=100)

    TYPE_CHOICES = [('radio', 'Radio'), ('checkbox', 'Checkbox')]
    answertype = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)

