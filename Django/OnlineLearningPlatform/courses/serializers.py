from rest_framework import serializers
from .models import Course,Content
from users.models import User

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','description','price']

    def validate_name(self,value):
        qs = Course.objects.filter(name__exact=value)
        if qs:
            raise serializers.ValidationError(f"'{value}' course already exists!")
        return value
     
class ContentCreateSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Content
        fields= ['title','content']
    def validate_title(self,value):
        qs = Content.objects.filter(title__exact=value)
        if qs:
            raise serializers.ValidationError(f"Content '{value}' already exists!")
        return value

class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    class Meta:
        model=Course
        fields=['course_id','teacher','name','description','created_at','updated_at','price']
    
    def get_teacher(self,obj):
        return obj.teacher.name

        
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        exclude = ['course',]