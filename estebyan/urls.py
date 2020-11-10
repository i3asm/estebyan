from django.contrib import admin
from django.urls import re_path, path, include
from forms import views

from estebyan.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', include(('forms.urls', 'forms'), namespace='forms')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup_view, name="register"),
    path('', views.pages, name='home'),

    # for static pages
    re_path(r'^.*\.*', views.pages, name='pages'),
]
