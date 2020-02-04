from django.urls import path
from .views import pollView

urlpatterns = [
    path('', pollView, name='index-view'),
]