from rest_framework import serializers
from .models import *

class NewUserSerialazer(serializers.Serializer):

    model = NewUser
    fields = "__all__"

