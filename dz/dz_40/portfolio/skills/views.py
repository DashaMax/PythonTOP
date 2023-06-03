from django.shortcuts import render

from skills.models import Skills


def index(request):
    projects = Skills.objects.all()
    context = {
        'title': 'Портфолио',
        'projects': projects
    }
    return render(request, 'skills/index.html', context=context)