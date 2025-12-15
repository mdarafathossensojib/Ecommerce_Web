from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductViewSet.as_view(), name='view-products'),
    path('<int:pk>/', views.ProductViewSet.as_view(), name='view-product'),
]
