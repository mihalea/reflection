from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

import logging

from .models import Project
from .forms import ProjectForm
from .utils.update import add as project_add, update as project_update

log = logging.getLogger(__name__)

def index(request):
    projects = Project.objects.all()
    return render(request, 'linker/index.html', {"projects" : projects})

def add(request, message=None):
    context = {}
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            repository = form.cleaned_data['repository']
            msg = project_add(username, repository)

            if msg:
                context['message'] = msg;
            else:
                return redirect('linker:index')
    else:
        form = ProjectForm()

    context['form'] = form
    return render(request, 'linker/add.html', context)

def update(request):
    username = request.GET.get("u")
    repository = request.GET.get("r")

    if username and repository:
        project_update(username, repository)
    else:
        log.warning("Invalid GET arguments, could not find username" +
            " and repository")

    return redirect('linker:index')
