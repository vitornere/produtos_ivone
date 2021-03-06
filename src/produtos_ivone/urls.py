"""produtos_ivone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import index, natura, demillus, odorata, avon, tupperware

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^natura$', natura, name='natura'),
    url(r'^demillus$', demillus, name='demillus'),
    url(r'^odorata$', odorata, name='odorata'),
    url(r'^avon$', avon, name='avon'),
    url(r'^tupperware$', tupperware, name='tupperware'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('sistema_usuario.urls')),
    url(r'', include('revista.urls')),
]
