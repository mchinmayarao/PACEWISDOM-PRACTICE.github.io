from django.urls import path
from .views import CourseListCreateView, CourseDetailView, ContentListCreateView, ContentDetailView,SubscribersListView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<str:name>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<str:name>/subscribers/', SubscribersListView.as_view(), name='subscribers-detail'),
    path('courses/<str:name>/contents/', ContentListCreateView.as_view(), name='content-list-create'),
    path('courses/<str:name>/contents/<str:title>/', ContentDetailView.as_view(), name='content-detail'),
]