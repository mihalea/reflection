from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'linker/index.html', {"projects" : projects})

def add(request):
    return render(request, 'linker/add.html')

def add_action(request):
    return HttpResponse("ADD")
