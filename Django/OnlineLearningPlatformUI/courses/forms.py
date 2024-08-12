from django import forms
from .models import Course, Content

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description','price']

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'content']