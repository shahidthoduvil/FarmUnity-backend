from django.db.models import Count
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView,ListAPIView,CreateAPIView,DestroyAPIView,ListCreateAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from Account.permision import IsAuthenticatedWithToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class FollowView(APIView):
    def get(self,request,user1,user2):
        instance=Follow.objects.filter(following_user__id=user1,followed_user__id=user2)
        is_followed=True if instance.exists() else False
        status_code=200 if is_followed else 404

        print('status===',status_code)
        return Response(data={"is_followed":is_followed},status=status_code)
    
    def post(self, request, user1, user2):
        try:
            following_user = User.objects.get(id=user1)
            followed_user = User.objects.get(id=user2)
            Follow.objects.create(
                following_user=following_user, followed_user=followed_user
            )
        except Exception as e:
            print(e,'eeeeeeeeeeeeeeeeeeeeeeeee')
            return Response(status=400, data={'error': str(e)})
        return Response(status=201)
    

    def delete(self,request,user1,user2):
        instance=Follow.objects.filter(
            following_user__id=user1,followed_user__id=user2
        )
        if instance.exists():
            instance.delete()
            return Response(status=200)

