from rest_framework import serializers
from .models import Course,Content
from users.models import User

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','description','price']
     


class ContentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields= ['title','content']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"
        
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields="__all__"