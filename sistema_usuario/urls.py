from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^login/', views.login, name='login'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^perfil/', views.perfil, name= 'perfil'),
	url(r'^editar/', views.editar, name='editar'),
]