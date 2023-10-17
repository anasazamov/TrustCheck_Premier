from rest_framework import serializers
from .models import *

class NewUserSerialazer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"

class TokenSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=255)

