from . import views
from django.urls import path

urlpatterns = [
    path('catalogue/', views.CoffeeList.as_view(), name='catalogue'),
]