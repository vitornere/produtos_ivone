from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

def login(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		senha = request.POST['senha']
		user = autenticate(username=usuario, password=senha)
	else:
		return render(request, 'sistema_usuario/login.html', {})


def signup(request):
	return render(request, 'sistema_usuario/signup.html', {})


def logout(request):
	return HttpResponseRedirect('/index/')
