from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<slug:post>/', views.product_detail, name='product_detail'),
]
