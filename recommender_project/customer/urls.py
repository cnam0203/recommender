from django.urls import path
from . import views

urlpatterns = [
    path('greeting', views.get_list_customers),
]