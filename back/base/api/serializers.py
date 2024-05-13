from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import *

from django.contrib.auth.models import User, Group

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.auth.hashers import make_password


class LicenseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseModel
        fields = "__all__"
        extra_kwargs = {'key': {'read_only': True}}

    def create(self, validated_data):
        license_instance = LicenseModel.objects.create(**validated_data)
        self.send_license_email(license_instance)
        return license_instance

    def send_license_email(self, license_instance):
        user = license_instance.user
        if user:
            email = user.email
            html_content = render_to_string('email_license.html', {'license_uuid': license_instance.key, 'name': license_instance.name})
            text_content = strip_tags(html_content)
            send_mail(
                subject="Вот ваша лицензия",
                message=text_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                html_message=html_content,
                fail_silently=False,
            )
        else:
            # По хорошему тут надо описать что происходит если почта не связана, но такого произойти не может
            pass




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = "__all__"