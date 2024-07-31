from django.contrib import admin
from .models import Content,Course
# Register your models here.
# admin.site.register(Content)
# admin.site.register(Course)

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1 

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'teacher')
    search_fields = ('name', 'description')
    inlines = [ContentInline]  

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'added_at')
    search_fields = ('title', 'course__name')  

admin.site.register(Course, CourseAdmin)
admin.site.register(Content, ContentAdmin)
