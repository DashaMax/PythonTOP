from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles_ = Profile.objects.all()
    context = {
        'profiles': profiles_
    }
    return render(request, 'users/index.html', context=context)
