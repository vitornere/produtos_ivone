from django.shortcuts import render

def index(request):
    revista = None
    return render(request, 'produtos_ivone/index.html', {'revista': revista})


def natura(request):
    revista = 'media/revistas/Natura.pdf'
    return render(request, 'produtos_ivone/index.html', {'revista': revista})


def demillus(request):
    revista = 'media/revistas/Demillus.pdf'
    return render(request, 'produtos_ivone/index.html', {'revista': revista})


def odorata(request):
    revista = 'media/revistas/Odorata.pdf'
    return render(request, 'produtos_ivone/index.html', {'revista': revista})


def avon(request):
    revista = 'media/revistas/Avon.pdf'
    return render(request, 'produtos_ivone/index.html', {'revista': revista})


def tupperware(request):
    revista = 'media/revistas/Tupperware.pdf'
    return render(request, 'produtos_ivone/index.html', {'revista': revista})
