from django.shortcuts import render

def index(request):
	return render(request, 'produtos_ivone/index.html', {})