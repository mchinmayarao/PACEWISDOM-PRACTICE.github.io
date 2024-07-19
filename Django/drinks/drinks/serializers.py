from .models import Drinks
from rest_framework import serializers


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = "__all__"
