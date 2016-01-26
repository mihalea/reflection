from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

import logging

from .models import Project
from .forms import ProjectForm
from .utils.update import add as project_add, update as project_update

log = logging.getLogger(__name__)

def index(request):
    log.debug("Index dispatchted");
    projects = Project.objects.all()
    return render(request, 'linker/index.html', {"projects" : projects})

@staff_member_required
def add(request, message=None):
    log.debug("Add dispatchted");
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

@staff_member_required
def update(request):
    log.debug("Update dispatched");
    username = request.GET.get("username")
    repository = request.GET.get("repository")

    if username and repository:
        project_update(username, repository)
    else:
        log.warning("Invalid GET arguments, could not find username" +
            " and repository")

    return redirect('linker:index')

@staff_member_required
def view(request, id):
    log.debug("View dispatched");
    project = get_object_or_404(Project, id=id)
    log.debug("Project " + project.username + "/" + project.repository + " has been requested")
    return render(request, 'linker/view.html', {'project': project})
