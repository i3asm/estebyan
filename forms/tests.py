from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from .models import Form, Question, Reply, Answer
from django.forms import modelformset_factory
from .forms import QuestionForm
from .views import add_questions


class FormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        f = Form.objects.create(name="test1", pub_date=timezone.now(), description="des", without_login=True,
                                user=self.user)
        q = Question.objects.create(text="what's your name", form=f)
        r = Reply.objects.create(form=f)
        a = Answer.objects.create(text="ahmed", question=q, reply=r)

    def test_forms_exist(self):
        f = Form.objects.get(id=1)
        q = Question.objects.get(id=1)
        r = Reply.objects.get(id=1)
        a = Answer.objects.get(id=1)

        self.assertEqual(f.reply_set.first(), r)
        self.assertEqual(f.question_set.first(), q)
        self.assertEqual(q.answer_set.first(), a)

    def test_question_formset(self):
        question_formset = modelformset_factory(Question, fields=['text'], extra=1)
        data = {'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 1,
                'form-MIN_NUM_FORMS': 0,
                'form-MAX_NUM_FORMS': 1000,
                'form-0-text': "what's your name",
                'form-0-id': 2,
                'form-1-text': "hi you",
                'form-1-id': '',
                }
        # response = self.client.post('/forms/21/edit/addQ', data)
        for form in question_formset(data):
            print(form.errors)

        print(Question.objects.all())
