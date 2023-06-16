"""
Login related functionality will go in this file
"""
from django.contrib.auth import login

from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView
from user.serializer import UserLoginSerializer




class LoginView(KnoxLoginView):
    """
    This view is for logging user in the application which will return token in the response
    Token is used in every API in the headers
    Authorization Token <Toke-generated-after-log-in>
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request)
