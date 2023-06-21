from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .form import CustomUserCreationForm


def profiles(request):
    profiles_ = Profile.objects.all()
    context = {
        'profiles': profiles_
    }
    return render(request, 'users/index.html', context=context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')
    context = {
        'profile': profile,
        'skills': skills,
        'other_skills': other_skills,
    }
    return render(request, 'users/profile.html', context=context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def register(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during register')

    context = {
        'page': page,
        'form': form,
    }

    return render(request, 'users/login_register.html', context=context)


@login_required
def account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }

    return render(request, 'users/account.html', context=context)


@login_required
def edit_account(request):
    return render(request, 'users/profile_form.html')