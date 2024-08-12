from django.urls import path
from .views import (
    CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView,
    ContentListView, ContentCreateView, ContentDetailView, ContentUpdateView, ContentDeleteView,

)

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/<str:name>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<str:name>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('courses/<str:name>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('courses/<str:name>/contents/', ContentListView.as_view(), name='content_list'),
    path('courses/<str:name>/contents/create/', ContentCreateView.as_view(), name='content_create'),
    path('courses/<str:name>/contents/<int:pk>/', ContentDetailView.as_view(), name='content_detail'),
    path('courses/<str:name>/contents/<int:pk>/update/', ContentUpdateView.as_view(), name='content_update'),
    path('courses/<str:name>/contents/<int:pk>/delete/', ContentDeleteView.as_view(), name='content_delete'),

]
    