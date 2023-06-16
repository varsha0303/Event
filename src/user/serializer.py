"""
Login and user related serializers should be added here
"""
from django.contrib.auth import (authenticate)
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):  # pylint: disable=W0223
    """
    User Login Serializer
    """
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
