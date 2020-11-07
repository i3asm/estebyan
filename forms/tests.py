from django.test import TestCase
from django.utils import timezone
from .models import Form, Question, Reply, Answer


class FormTestCase(TestCase):
    def setUp(self):
        f = Form.objects.create(name="test1", pub_date=timezone.now())
        q = Question.objects.create(text="what's your name", form=f)
        r = Reply.objects.create(form=f)
        a = Answer.objects.create(text="ahmed", question=q, reply=r)

    def test_forms_exist(self):
        f = Form.objects.get(id=1)
        q = Question.objects.get(id=1)
        r = Reply.objects.get(id=1)
        a = Answer.objects.get(id=1)

        self.assertEqual(f.replies().first(), r)
        self.assertEqual(f.questions().first(), q)
        self.assertEqual(q.answers().first(), a)
        self.assertEqual(r.answers().first(), a)
