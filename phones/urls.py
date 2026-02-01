from django.urls import path
from . import views

app_name = 'phones'

urlpatterns = [
    path('', views.phone_list, name='phone-list'),
    path('<slug:slug>/', views.phone_detail, name='phone-detail'),
]