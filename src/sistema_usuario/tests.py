import pytest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .views import login


class TestUsers():
    @pytest.mark.django_db
    def test_create_user_with_sucess(self):
        user = User.objects.create_user('joao', 'joao@email.com', 'joao123')
        user.first_name = 'João'
        user.last_name = 'José'
        user.save()
        assert authenticate(username='joao', password='joao123') is not None


class TestViews():
    @pytest.fixture
    def user(self, db):
        user = User.objects.create_user('joao', 'joao@email.com', 'joao123')
        user.first_name = 'João'
        user.last_name = 'José'
        user.save()
        return user

    def test_get_login(self, client):
        response = client.get('/login/')
        assert response.status_code == 200

    def test_post_login_with_sucess(self, client, db):
        response = client.post(
            '/login/', {'usuario': 'joao', 'senha': 'joao123'})
        assert response.status_code == 200

    def test_post_login_without_args(self, client, db):
        response = client.post('/login/', {'usuario': 'joao', 'senha': ''})
        assert response.status_code == 200
