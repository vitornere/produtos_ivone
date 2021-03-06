# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return render(request, 'sistema_usuario/home.html')


def login(request):
    if request.method == 'POST':
        # POST
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        if usuario == "" or senha == "":
            return render(request, 'sistema_usuario/login.html', {'erro': 'Preencha todos os campos.'})

        user = authenticate(username=usuario, password=senha)
        if user is not None:
            # Fazer Login
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            # Autenticação inválida
            return render(request, 'sistema_usuario/login.html', {'erro': 'Usuário e/ou Senha inválidos.'})
    else:
        # GET
        return render(request, 'sistema_usuario/login.html', {})


def signup(request):
    if request.method == 'POST':
        # POST
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if nome == "" or sobrenome == "" or email == "" or nome_usuario == "" or senha == "" or confirmar_senha == "":
            return render(request, 'sistema_usuario/signup.html', {'erro': 'Preencha todos os campos.'})
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'sistema_usuario/signup.html', {'erro': 'Email inválido'})
        if senha == confirmar_senha:
            # Fazer Cadastro
            user = User.objects.create_user(nome_usuario, email, senha)
            user.first_name = nome
            user.last_name = sobrenome
            user.save()
            user = authenticate(username=nome_usuario, password=senha)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'sistema_usuario/signup.html', {'erro': 'Algo deu muito errado.'})
        else:
            return render(request, 'sistema_usuario/signup.html', {'erro': 'As senhas não conferem.'})

    else:
        # GET
        return render(request, 'sistema_usuario/signup.html', {})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def perfil(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/editar/')
    else:
        if request.user.is_authenticated():
            return render(request, 'sistema_usuario/perfil.html')
        else:
            return HttpResponseRedirect('/')


def editar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if nome == "" or sobrenome == "" or email == "" or nome_usuario == "":
            return render(request, 'sistema_usuario/editar.html', {'erro': 'Preencha todos os campos.'})
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'sistema_usuario/editar.html', {'erro': 'Email inválido'})

        # Atualiza Cadastro
        if senha != confirmar_senha:
            return render(request, 'sistema_usuario/editar.html', {'erro': 'As senhas não conferem.'})
        else:
            if senha == "" and confirmar_senha == "":
                user = request.user
                user.first_name = nome
                user.last_name = sobrenome
                user.email = email
                user.nome_usuario = nome_usuario
                user.save()
            else:
                user = request.user
                user.first_name = nome
                user.last_name = sobrenome
                user.email = email
                user.nome_usuario = nome_usuario
                user.set_password(senha)
                user.save()

        return render(request, 'sistema_usuario/editar.html')
    else:
        if request.user.is_authenticated():
            return render(request, 'sistema_usuario/editar.html')
        else:
            return HttpResponseRedirect('/')
