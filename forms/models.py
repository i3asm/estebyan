from django.db import models
from django.conf import settings


class Form(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True)
    pub_date = models.DateTimeField('date published')
    without_login = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Reply(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
