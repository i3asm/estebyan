from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import template
from .models import Form, Question, Reply, Answer
from .forms import FormForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    forms = Form.objects.filter(user_id=request.user.id).order_by('-pub_date')
    context = {
        'forms': forms
    }
    return render(request, 'forms/index.html', context)


@login_required()
def create(request):
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            tmp = Form.objects.create(name=form.cleaned_data['name'], pub_date=timezone.now(),
                                      user_id=request.user.id).id
            # return redirect('forms:show', id=tmp)
            return redirect('forms:index')

    else:
        form = FormForm()
        context = {
            'form': form
        }
        return render(request, 'forms/create.html', context)


def show(request, id):
    return HttpResponse(Form.objects.get(id=id).question_set.all())


@login_required()
def edit(request, id):
    return HttpResponse(Form.objects.get(id=id))


@login_required()
def delete(request, id):
    form = Form.objects.get(id=id)
    print(form)
    if form.user_id == request.user.id:
        print(form.delete())
    return redirect('forms:index')


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
