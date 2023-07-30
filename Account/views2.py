from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from rest_framework import status
from .tocken import create_jwt_pair_tokens
from rest_framework.generics import UpdateAPIView

from .models import *

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serilizer import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter



class CategoryOccupationListView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category')
        
        # Fetch all categories
        categories=Category.objects.all()
        
        # If a category ID is provided in the request, filter occupations by that category
        if category_id:
          occupations = Occupation.objects.filter(Cat=category_id)
        else:
            # If no category ID is provided, return all occupations
         occupations = Occupation.objects.all()

        category_serializer = CategorySerilizer(categories, many=True)
        occupation_serializer =OccupationSerilizer(occupations, many=True)

        return Response({
            'categories': category_serializer.data,
            'occupations': occupation_serializer.data
        })

class UserProfileUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserProfileSerializer
    lookup_field = 'id'


class AddressUpdateView(UpdateAPIView):
   queryset=Address.objects.all()
   serializer_class=AccountSerilizer
   lookup_field='user__id'



class CheckProfileSetupView(APIView):


    def get(self, request, *args, **kwargs):
        try:
            print(request.data)

            user = User.objects.get(id=request.data.user)
         
            if user.is_setup_complete:
                # Profile setup is complete, return the serialized data

                user_profile_serializer = UserProfileSerializer(user)
                account_data = Address.objects.get(user=request.user)
                account_serializer = AccountSerilizer(account_data)
                return Response({
                    "detail": "Profile setup is complete.",
                    "user_profile": user_profile_serializer.data,
                    "account_data": account_serializer.data,
                }, status=status.HTTP_200_OK)
            else:
                # Profile setup is not complete
                return Response({"detail": "Profile setup is not complete."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
