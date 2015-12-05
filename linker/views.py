from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'linker/index.html', {"projects" : projects})
