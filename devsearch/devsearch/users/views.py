from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, authenticate, login


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
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    return redirect('login')