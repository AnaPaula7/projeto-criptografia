from django.urls import path
from .views import criptografia_view

urlpatterns = [
    path('', criptografia_view, name='criptografia'),
]
