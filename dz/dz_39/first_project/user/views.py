from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

import re

from first_app.models import PasswordModel


def registration(request):
    context = {
        'title': 'Регистрация',
        'form': UserCreationForm(),
        'error': None,
    }

    if request.method == 'POST':
        name = re.findall(r'[^а-яА-Яa-zA-Z0-9@.+_-]', request.POST['username'])
        password = re.findall(r'[^0-9]', request.POST['password1'])

        if len(request.POST['username']) < 3 or len(request.POST['username']) > 150 or name:
            context['error'] = 'Некорректное имя пользователя'

        elif len(request.POST['password1']) < 8:
            context['error'] = 'Ваш пароль слишком короткий'

        elif not password:
            context['error'] = 'Пароль не может состоять только из цифр'

        elif request.POST['password1'] != request.POST['password2']:
            context['error'] = 'Пароли не совпадают'

        else:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main')

            except IntegrityError:
                context['error'] = 'Пользователь с таким именем уже существует'

    return render(request, 'user/registration.html', context=context)


def get_logout(request):
    logout(request)
    return redirect('main')


def get_login(request):
    context = {
        'title': 'Авторизация',
        'form': AuthenticationForm(),
        'error': ''
    }

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if not user:
            context['error'] = 'Неверно введен логин или пароль'
            return render(request, 'user/login.html', context=context)

        login(request, user)
        return redirect('main')

    return render(request, 'user/login.html', context=context)


@login_required
def get_lk(request):
    context = {
        'title': 'Личный кабинет',
    }
    return render(request, 'user/lk.html', context=context)


@login_required
def add_password(request):
    context = {
        'error': '',
    }
    try:
        password = PasswordModel(password=request.POST['password'], user=request.user)
        password.save()
        return redirect('mypassword')
    except IntegrityError:
        context['error'] = 'Ошибка добавления в БД'
        return render(request, 'first_project/password.html', context=context)


@login_required
def get_mypassword(request):
    context = {
        'title': 'Мои пароли',
        'passwords': PasswordModel.objects.filter(user=request.user)
    }
    return render(request, 'user/mypassword.html', context=context)


@login_required
def delete(request, pk):
    password = PasswordModel.objects.get(id=pk)
    password.delete()
    return redirect('mypassword')
