from django.urls import path
from . import views

urlpatterns = [
    path('encrypt', views.encrypt, name='encrypt'),
    path('decrypt', views.decrypt, name='decrypt'),
]
