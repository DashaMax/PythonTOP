from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


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


@login_required(login_url='login')
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }

    return render(request, 'projects/form-template.html', context=context)
