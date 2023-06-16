from django.shortcuts import render
from .models import Project


def get_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context=context)


def get_project(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/single-project.html', context=context)
