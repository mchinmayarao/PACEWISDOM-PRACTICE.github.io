from .models import Drinks,CustomUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
      # extra_kwargs = {'password': {'write_only': True}} # When retriving the password must not be shown
    def create(self, validated_data):
 
        try:
            validate_email(validated_data['email'])
            validate_password(validated_data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"messages":e.messages})

        user = CustomUser(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        if password and email:
            try:
                validate_email(email)
                validate_password(password)
            except ValidationError as e :
                raise serializers.ValidationError({'messages': e.messages})
            instance.set_password(password)
        
        instance.email = email
        instance.save()
        return instance


        