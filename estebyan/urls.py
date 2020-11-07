from django.contrib import admin
from django.urls import re_path, path, include
from forms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', include(('forms.urls', 'forms'), namespace='forms')),
    path('logout/', views.index, name='logout'),
    path('', views.pages, name='home'),

    # for static pages
    re_path(r'^.*\.*', views.pages, name='pages'),
]
