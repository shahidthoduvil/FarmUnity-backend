from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from Account.serilizer import *


class UserByCategoryView(APIView):
    def get(self, request, categoryName):
        try:
            users = User.objects.filter(Occup__Cat__Category_name=categoryName)
           

            serializer =UserSerializer(users, many=True)


            return Response(serializer.data)
        except Exception as e:
            return Response({"message": f"Error fetching users by category.{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        





class SearchUsersByCategory(APIView):
    def get(self, request, categoryName):
        try:
            search_query = request.query_params.get('q', '')
            users = User.objects.filter(
                Occup__Cat__Category_name=categoryName,
                Occup__titile__icontains=search_query,
                username__icontains=search_query,
                first_name__icontains=search_query,
            )
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": f"Error searching users by category and occupation. {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)