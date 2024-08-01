from django.urls import path
from .views import adryan, bruno

urlpatterns = [
    path('', adryan, name='adryan'),
    path('bruno/', bruno, name='bruno')
]