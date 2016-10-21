from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

import logging

from .models import Project
from .forms import ProjectForm

log = logging.getLogger(__name__)


def index(request):
    return render(request, 'projects/index.html', {})


def showcase(request):
    log.debug("Index dispatched")
    context = {
        "featured": Project.objects.featured(),
        "not_featured": Project.objects.not_featured()
    }
    return render(request, 'projects/list.html', context)


@staff_member_required
def edit(request, slug):
    log.debug("Edit dispatched")

    instance = get_object_or_404(Project, slug=slug)
    form = ProjectForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            log.debug("Edited project: %s/%s" % (instance.username, instance.repository))
            return HttpResponseRedirect(instance.get_absolute_link())
        else:
            log.warning("Submitted form is not valid")

    context = {
        "form": form
    }
    return render(request, 'projects/add.html', context)


@staff_member_required
def add(request):
    log.debug("Add dispatched")

    form = ProjectForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            log.debug("Added new project: %s/%s" % (instance.username, instance.repository))
            return HttpResponseRedirect(instance.get_absolute_link())
        else:
            log.warning("Submitted form is not valid")

    context = {"form": form}
    return render(request, 'projects/add.html', context)


@staff_member_required
def update(request):
    log.debug("Update dispatched")
    username = request.GET.get("username")
    repository = request.GET.get("repository")

    if username and repository:
        pass
    else:
        log.warning("Invalid GET arguments, could not find username" +
                    " and repository")

    return redirect('projects:index')


@staff_member_required
def details(request, slug):
    log.debug("View dispatched");
    project = get_object_or_404(Project, slug=slug)
    log.debug("Project " + project.username + "/" + project.repository + " has been requested")
    return render(request, 'projects/view.html', {'project': project})
