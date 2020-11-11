from django.forms import ModelForm
from forms.models import Form


class FormForm(ModelForm):
    class Meta:
        model = Form
        fields = ['name']
