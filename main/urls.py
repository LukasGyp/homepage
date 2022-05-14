from django.urls import path

from . import views

urlpatterns = [
  path('', views.top, name='top'),
  path('profile', views.profile, name='profile'),
]