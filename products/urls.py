from django.urls import path
from . import views

urlpatterns = [
    # root url
    path('', views.all_products, name='products'),
]
