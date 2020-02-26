from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.survey + ": " + self.text


class Choice(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.survey + ": " + self.question + ": " + self.text


class Taken(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    student = models.CharField(max_length=20)
