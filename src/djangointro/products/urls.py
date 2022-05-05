from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_products, name='listProducts'),
    path('add/', views.create_products, name='createProduct')
]
