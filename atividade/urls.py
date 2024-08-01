from django.urls import path
from .views import adryan

urlpatterns = [
    path('', adryan, name='adryan')
]