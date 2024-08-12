from django.urls import path
from . import views
urlpatterns = [
    path("courses/<str:name>/checkout/",views.checkout,name='checkout'),
    path('api/orders', views.create_order, name='create_order'),
    path('api/orders/<str:order_id>/capture', views.capture_order, name='capture_order'),
]
