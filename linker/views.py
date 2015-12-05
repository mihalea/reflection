from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'linker/index.html', {"projects" : projects})

def show(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'linker/show.html', {"project" : project})
