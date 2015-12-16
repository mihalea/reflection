from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Project
from .forms import ProjectForm
from .utils.update import add as project_add

def index(request):
    projects = Project.objects.all()
    return render(request, 'linker/index.html', {"projects" : projects})

def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            repository = form.cleaned_data['repository']
            project_add(username, repository)
            #return redirect('linker:index')
    else:
        form = ProjectForm()

    return render(request, 'linker/add.html', {'form': form})
