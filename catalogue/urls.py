from . import views
from django.urls import path

urlpatterns = [
    path('catalogue/', views.CoffeeList.as_view(), name='Catalogue'),
    path('catalogue/<int:product_ID>/', views.coffee_detail, name='Coffee detail'),
]