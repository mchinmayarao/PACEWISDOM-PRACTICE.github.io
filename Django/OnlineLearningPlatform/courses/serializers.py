from rest_framework import serializers
from .models import Course,Content,Enrollment
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','description','price']

    def save(self, **kwargs):
        print(kwargs['teacher'])
        teacher = kwargs['teacher']
        subscribers = [student.email for student in User.objects.filter(enrollment__course__teacher=teacher).distinct()]
        print(subscribers)
        send_mail(
            f"New Course {self.validated_data['name']} Added!",
            f"""Hi Learner,

Good news! Instructor {teacher.name} just added a new course, {self.validated_data['name']}. Dive into the new Course and continue your learning journey.

Log in now and check it out!

Happy learning,
Online Learning Platform""",
            settings.DEFAULT_FROM_EMAIL,
            subscribers,
            fail_silently=False,
        )

        return super().save(**kwargs)

    def validate_name(self,value):
        qs = Course.objects.filter(name__exact=value)
        if qs:
            raise serializers.ValidationError(f"'{value}' course already exists!")
        return value
     
class ContentCreateSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Content
        fields= ['title','content']
    
    def save(self, **kwargs):
        course = kwargs.get('course')
        enrollment = Enrollment.objects.filter(course = course)
        subscribers = [entry.student.email for entry in enrollment]
       
        print(self.validated_data)
        send_mail(
            f"Course Update {course.name}!",
            f"""Hi Learner,

Good news! The teacher just added fresh content to your course, {course.name}. Dive into the new content and continue your learning journey.

Log in now and check it out!

Happy learning,
Online Learning Platform""",
            settings.DEFAULT_FROM_EMAIL,
            subscribers,
            fail_silently=False,
        )

        return super().save(**kwargs)
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