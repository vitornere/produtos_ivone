from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^login/', views.login, name='login'),
]