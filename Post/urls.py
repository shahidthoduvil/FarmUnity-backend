from django.urls import path
from .views import *

urlpatterns = [
 
    path('posts/',PostListCreateView.as_view(), name='post-list-create'),
]

