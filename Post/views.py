
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView,ListAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from Account.permision import IsAuthenticatedWithToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.


    
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

