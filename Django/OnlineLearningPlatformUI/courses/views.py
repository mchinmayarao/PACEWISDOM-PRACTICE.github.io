from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course, Content, Enrollment
from .forms import CourseForm, ContentForm
from .decorators import is_teacher, is_owner, is_enrolled_or_teacher
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
@method_decorator(is_teacher, name='dispatch')
class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')


    def form_valid(self, form):
        form.instance.teacher = self.request.user
        messages.success(self.request, f'{form.instance.name} created successfully!')
        return super().form_valid(form)

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        user = self.request.user


        if user.is_authenticated:
            try:
                enrollment = Enrollment.objects.get(course=course, student=user)
                context['is_enrolled'] = True
                context['status'] = enrollment.status
            except Enrollment.DoesNotExist:
                context['is_enrolled'] = False
                context['status'] = 'not_enrolled'
        else:
            context['is_enrolled'] = False
            context['status'] = 'not_logged_in'
        return context


    def get_object(self, queryset=None):
        name = self.kwargs['name']  
        return get_object_or_404(Course, name=name)


@method_decorator(is_owner, name='dispatch')
class CourseUpdateView(LoginRequiredMixin, UpdateView):
    """_summary_

    Args:
        LoginRequiredMixin (_type_): _description_
        UpdateView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = Course
    form_class = CourseForm 
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')
    def get_object(self, queryset=None):
        name = self.kwargs['name']  
        return get_object_or_404(Course, name=name)
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'{self.kwargs['name']} updated successfully!')
        return response

@method_decorator(is_owner, name='dispatch')
class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('dashboard')
    def get_object(self, queryset=None):
        name = self.kwargs['name']  
        return get_object_or_404(Course, name=name)
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'{self.kwargs['name']} deleted successfully!')
        return response
    
@method_decorator(is_enrolled_or_teacher, name='dispatch')
class ContentListView(ListView):
    model = Content
    template_name = 'content_list.html'
    context_object_name = 'contents'

    def get_queryset(self):
        course_name = self.kwargs['name']
        course = get_object_or_404(Course, name=course_name)
        return Content.objects.filter(course=course)
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(name = self.kwargs['name'])
        return context

@method_decorator(is_owner, name='dispatch')
class ContentCreateView(LoginRequiredMixin, CreateView):
    model = Content
    form_class = ContentForm
    template_name = 'content_form.html'
    success_url = reverse_lazy('course_detail')

    def form_valid(self, form):
        course_name = self.kwargs['name']
        course = get_object_or_404(Course, name=course_name)
        form.instance.course = course
        self.success_url = reverse_lazy('content_list', kwargs={'name': course_name})
        messages.success(self.request, f'Content for {course_name} created successfully!')
        return super().form_valid(form)

@method_decorator(is_enrolled_or_teacher, name='dispatch')
class ContentDetailView(LoginRequiredMixin,DetailView):
    model = Content
    template_name = 'content_detail.html'
    context_object_name = 'content'

    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        # context['course'] = Content.object
        return context

@method_decorator(is_owner, name='dispatch')
class ContentUpdateView(LoginRequiredMixin, UpdateView):
    model = Content
    form_class = ContentForm
    template_name = 'content_form.html'
    success_url = reverse_lazy('content_list')

@method_decorator(is_owner, name='dispatch')
class ContentDeleteView(LoginRequiredMixin, DeleteView):
    model = Content
    def get_success_url(self):
        course_name = self.object.course.name
        return reverse_lazy('content_list', kwargs={'name': course_name})
    def form_valid(self, form):
        messages.success(self.request, f'Content  deleted successfully!')
        return super().form_valid(form)
    

