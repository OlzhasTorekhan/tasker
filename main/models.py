from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

class User(AbstractUser):
    number = models.CharField(max_length=25)

class UserSerilizers(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    description = serializers.CharField()