from django.urls import path
from .views import save_user
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', save_user, name='base')
]