from django.urls import path
from .views import register, login, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('notes/', profile, name='user-notes'),
]