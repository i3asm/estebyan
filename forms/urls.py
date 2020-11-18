from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:id>', views.show, name='show'),
    path('<int:id>/preview', views.preview, name='preview'),
    path('<int:id>/reply', views.reply, name='reply'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:form_id>/edit/createQ', views.create_question, name='create_question'),
    path('<int:form_id>/edit/editQ/<int:question_id>', views.edit_question, name='edit_question'),
    path('<int:form_id>/edit/deleteQ/<int:question_id>', views.delete_question, name='delete_question'),
]
