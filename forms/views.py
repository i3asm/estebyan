from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import template
from .models import Form, Question, Reply, Answer


def index(request):
    forms = Form.objects.order_by('-pub_date').all()
    context = {
        'forms': forms
    }
    return render(request, 'forms/index.html', context)


def create(request):
    forms = Form.objects.order_by('-pub_date').all()
    context = {
        'forms': forms
    }
    return render(request, 'forms/create.html', context)


def show(request, id):
    return HttpResponse(Form.objects.get(id=id))


def edit(request, id):
    return HttpResponse(Form.objects.get(id=id))


def pages(request):
    context = {}

    # for home page requests:
    if request.path == '/' or request.path == 'home':
        return render(request, 'index.html')

    # for other page requests, try to find a template matching the name
    try:
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
