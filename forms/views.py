from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django import template
from .models import Form, Question
from .forms import FormForm, QuestionForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@login_required()
def index(request):
    forms = Form.objects.filter(user=request.user).order_by('-pub_date')
    context = {
        'forms': forms
    }
    return render(request, 'forms/index.html', context)


@login_required()
def create(request):
    if request.method == 'POST':
        form = FormForm(request.POST)
        if form.is_valid():
            Form.objects.create(name=form.cleaned_data['name'], pub_date=timezone.now(),
                                user_id=request.user.id, description=form.cleaned_data['description'])
            return redirect('forms:index')
        else:
            return redirect('forms:index')
    else:
        return render(request, 'page-404.html')


@login_required()
def show(request, id):
    try:
        form = Form.objects.get(id=id, user=request.user)
    except Form.DoesNotExist:
        raise Http404("الاستبيان غير موجود")
    context = {
        'form': form
    }
    return render(request, 'forms/show.html', context)


@login_required()
def edit(request, id):
    if Form.objects.get(id=id).user != request.user:
        return render(request, 'page-403.html')
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
        }
        return render(request, 'forms/edit.html', context)


@login_required()
def delete(request, id):
    form = Form.objects.get(id=id)
    if form.user != request.user:
        return render(request, 'page-403.html')
    else:
        form.delete()
    return redirect('forms:index')


@login_required()
def create_question(request, form_id):
    if Form.objects.get(id=form_id).user != request.user:
        return render(request, 'page-403.html')
    if request.method == 'POST':
        question = QuestionForm(request.POST)
        if question.is_valid():
            Question.objects.create(form_id=form_id, text=question.cleaned_data['text'])
        return redirect('forms:edit', form_id)


def edit_question(request, form_id, question_id):
    if Form.objects.get(id=form_id).user != request.user:
        return render(request, 'page-403.html')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(id=question_id)
            question.text = form.cleaned_data['text']
            question.save()
        return redirect('forms:edit', form_id)
    else:
        return redirect('forms:edit', form_id)


def delete_question(request, form_id, question_id):
    if Form.objects.get(id=form_id).user != request.user:
        return render(request, 'page-403.html')
    if request.method == 'POST':
        Question.objects.get(id=question_id).delete()
        return redirect('forms:edit', form_id)
    else:
        return redirect('forms:edit', form_id)


def preview(request, id):
    pass


def reply(request, id):
    pass


def handler403(request, exception):
    return render(request, 'page-403.html', status=403)


def handler404(request, exception):
    return render(request, 'page-404.html', status=404)


def handler500(request):
    return render(request, 'page-500.html', status=500)


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
