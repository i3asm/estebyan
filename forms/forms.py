from django.forms import ModelForm
from forms.models import Form, Question


class FormForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']
