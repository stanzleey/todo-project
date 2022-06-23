from django.urls import path

# import my_view from todo Application
from .views import my_view

urlpatterns = [
    path('', my_view, name='my_view')
]