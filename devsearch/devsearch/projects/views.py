from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, ReviewForm
from .utils import search_projects, paginate_projects


def get_projects(request):
    projects, search_query = search_projects(request)
    custom_range, projects = paginate_projects(request, projects, 3)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context=context)


def get_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.get_vote_count()
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=project.id)

    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'projects/single-project.html', context=context)


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }

    return render(request, 'projects/form-template.html', context=context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form
    }

    return render(request, 'projects/form-template.html', context=context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('account')

    context = {
        'project': project,
    }

    return render(request, 'projects/delete.html', context=context)