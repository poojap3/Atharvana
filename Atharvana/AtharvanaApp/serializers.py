from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username','password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class TaskValueSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskValue
        fields="__all__"
