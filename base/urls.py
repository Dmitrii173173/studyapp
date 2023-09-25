from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<str:pk>/', views.product, name="product"),
    path('create-product/', views.createProduct, name="create-product"),
    path('create-lesson/', views.createLesson, name="create-lesson"),
    path('update-lesson/<str:pk>/', views.updateLesson, name="update-lesson"),
    path('delete-lesson/<str:pk>/', views.deleteLesson, name="delete-lesson"),
]