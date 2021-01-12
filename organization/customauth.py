from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate, get_user_model

class CustomAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed(('Enter proper credentials'))

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)
        
        if user is None:
            raise exceptions.AuthenticationFailed(('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(('No Such User or deleted'))

        return (user, None)



