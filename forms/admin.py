from django.contrib import admin

from .models import Form, Question, Reply, Answer

admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(Answer)
