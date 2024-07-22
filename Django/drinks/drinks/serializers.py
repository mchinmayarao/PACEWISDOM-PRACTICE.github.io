from .models import Drinks
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
      # extra_kwargs = {'password': {'write_only': True}} # When retriving the password must not be shown
    def create(self, validated_data):
 
        try:
            validate_password(validated_data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"messages":e.messages})

        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):

        password = validated_data.get('password')
        if password:
            try:
                validate_password(password)
            except ValidationError as e :
                raise serializers.ValidationError({'messages': e.messages})
            instance.set_password(password)
        
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


        