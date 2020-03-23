from django import forms


class QuestionForm(forms.Form):
    questiontext = forms.CharField(label='Question text', max_length=200)

    choice1text = forms.CharField(label='Choice 1', max_length=100)
    choice2text = forms.CharField(label='Choice 2', max_length=100)

    TYPE_CHOICES = [('radio', 'Radio'), ('checkbox', 'Checkbox')]
    answertype = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)

