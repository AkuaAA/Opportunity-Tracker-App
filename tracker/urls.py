from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='tracker-home'),
    path('customer_project/', views.customer_project, name='tracker-customer_project'),
]