from django.urls import path
from product import views

urlpatterns = [
    path('', views.CategoryViewSet.as_view(), name='category-list'),
    path('<int:pk>/', views.CategoryViewSet.as_view(), name='view-specific-category'),
]
