from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice


def get_main(request):
    length = list(range(6, 17))
    context = {
        'title': 'Генератор паролей',
        'length': length,
        'checkboxes': [
            ('uppercase', 'Верхний регистр'),
            ('digital', 'Цифры'),
            ('special', 'Символы пунктуации')
        ]
    }
    return render(request, 'first_app/main.html', context=context)


def get_password(request):
    chars = ascii_lowercase
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chars += ascii_uppercase

    if request.GET.get('digital'):
        chars += digits

    if request.GET.get('special'):
        chars += punctuation

    password = ''.join(choice(chars) for _ in range(length))
    context = {
        'title': 'Ваш пароль',
        'password': password
    }
    return render(request, 'first_app/password.html', context=context)


def get_info(request):
    context = {
        'title': 'Информация'
    }
    return render(request, 'first_app/info.html', context=context)