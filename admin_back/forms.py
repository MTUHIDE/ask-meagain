from django import forms


class QuestionForm(forms.Form):
    # will default to 2 choice questions, use add choice function on page to add more
    defaultChoices = 2

    text = forms.CharField(label='Question text', max_length=200)
    # choices stored in array to allow for extra choices to be added
    choices = []
    for i in range(defaultChoices):
        choices[i] = forms.CharField(label='Choice', max_length=100)

    TYPE_CHOICES = [('radio', 'Radio'), ('checkbox', 'Checkbox')]
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)

