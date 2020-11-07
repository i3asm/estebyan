from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def replies(self):
        return self.reply_set.all()

    def questions(self):
        return self.question_set.all()


class Question(models.Model):
    text = models.CharField(max_length=200)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def answers(self):
        return self.answer_set.all()


class Reply(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
