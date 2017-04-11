from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

def login(request):
	if request.method == 'POST':
		# POST
		usuario = request.POST['usuario']
		senha = request.POST['senha']
		user = authenticate(username=usuario, password=senha)
		if user is not None:
			# Fazer Login
			auth_login(request, user)
			return HttpResponseRedirect('/')
		else:
			# Autenticação inválida
			return render(request, 'sistema_usuario/login.html', {'erro':'Usuário e/ou Senha inválidos.'})
	else:
		# GET
		return render(request, 'sistema_usuario/login.html', {})


def signup(request):
	return render(request, 'sistema_usuario/signup.html', {})


def logout(request):
	return HttpResponseRedirect('/')
