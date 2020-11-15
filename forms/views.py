from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import template
from .models import Form, Question
from .forms import FormForm, QuestionForm
from django.forms import modelformset_factory, TextInput
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
                                      user_id=request.user.id, description=form.cleaned_data['description']).id
            # return redirect('forms:show', id=tmp)
            return redirect('forms:index')
        else:
            return redirect('forms:index')
    else:
        context = {
            'form': FormForm()
        }
        return render(request, 'forms/create.html', context)


def show(request, id):
    context = {
        'form': Form.objects.get(id=id)
    }
    return render(request, 'forms/show.html', context)


@login_required()
def edit(request, id):
    # TODO: make editing & deleting available only for the owner
    question_formset = add_questions(request, id)
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            tmp = Form.objects.get(id=id)
            tmp.name = form.cleaned_data['name']
            tmp.description = form.cleaned_data['description']
            tmp.save()
        return redirect('forms:edit', id=id)

    else:
        context = {
            'form': Form.objects.get(id=id),
            'formset': question_formset(queryset=Question.objects.filter(form_id=id)),
        }
        return render(request, 'forms/edit.html', context)


@login_required()
def add_questions(request, id):
    question_formset = modelformset_factory(Question, fields=['text'], extra=1, widgets={
        'text': TextInput(attrs={'class': 'form-control'})
    })
    if request.method == 'POST':
        formset = question_formset(request.POST)
        for form in formset:
            if form.is_valid():
                question = form.save(commit=False)
                question.form_id = id
                question.text = form.cleaned_data['text']
                question.save()
        return redirect('forms:edit', id)
    else:
        return question_formset


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
