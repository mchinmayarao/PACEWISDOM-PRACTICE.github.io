from django.urls import path
from .views import CourseListCreateView, CourseDetailView, ContentListCreateView, ContentDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<str:name>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<str:name>/contents/', ContentListCreateView.as_view(), name='content-list-create'),
    path('courses/<str:name>/contents/<int:pk>/', ContentDetailView.as_view(), name='content-detail'),
]