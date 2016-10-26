from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

import logging

from .models import Project
from .forms import ProjectForm
from .utils.update import update as update_data

log = logging.getLogger(__name__)


def index(request):
    return render(request, 'projects/index.html', {
        "links": settings.LINKS
    })


def about(request):
    return render(request, 'projects/about.html', {})


def contact(request):
    return render(request, 'projects/contact.html', {
        "links": settings.LINKS
    })


def showcase(request):
    log.debug("Index dispatched")
    context = {
        "featured": Project.objects.featured(),
        "not_featured": Project.objects.not_featured().order_by("updated_at")
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
def delete(request, slug):
    log.debug("Delete dispatched")

    instance = get_object_or_404(Project, slug=slug)
    instance.delete()

    return redirect("projects:showcase")


@staff_member_required
def update(request, slug):
    log.debug("Update dispatched")

    instance = get_object_or_404(Project, slug=slug)
    update_data(instance)

    return redirect("projects:view", slug=slug)


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


def details(request, slug):
    log.debug("View dispatched");
    project = get_object_or_404(Project, slug=slug)

    if not project.readme:
        return HttpResponseRedirect("http://github.com/%s/%s/" % (project.username, project.repository))

    log.debug("Project " + project.username + "/" + project.repository + " has been requested")
    return render(request, 'projects/view.html', {'project': project})
