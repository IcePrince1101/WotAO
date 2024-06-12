from .views import *
from django.urls import path

urlpatterns = [
    path('main/', main_view, name='main'),
    path('authorisation/', main_view, name='authorisation'),  # Warning: view not ready, only path
    path('registration/', main_view, name='registration'),  # Warning: view not ready, only path
    path('actvities/', main_view, name='activities'),  # Warning: view not ready, only path
    path ('contacts/', main_view, name='contacts'),  # Warning: view not ready, only path

]
