from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name= "home"),
    path('<int:contact_id>/', views.HomeView.as_view(), name= "contact")
]
