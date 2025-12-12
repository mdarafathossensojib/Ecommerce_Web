from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('orders/', include('order.urls')),
    path('products/', include('product.urls')),
    path('users/', include('users.urls')),
]
