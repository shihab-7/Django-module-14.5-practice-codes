from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('model/', views.goto, name='modelform'),
]