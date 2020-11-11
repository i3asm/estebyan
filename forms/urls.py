from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.delete, name='delete'),
]
