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
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from rest_framework.response import Response
from .serilizer import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter
from .helpers import authenticate_user
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings




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


@api_view(['GET'])
def check_profile_setup(request,id):

    try:
        user = User.objects.get(id=id)
        is_setup_complete = user.is_setup_complete
    except:
        return Response({"Error": 'Some error occured'})
    return Response({"is_setup_complete": is_setup_complete})



@api_view(["POST"])
@csrf_exempt
def is_user(request):
    isVerified = authenticate_user(request, "user")
   
    print("user verification", isVerified)
    return JsonResponse(isVerified is not None, safe=False)


@api_view(["POST"])
@csrf_exempt
def is_admin(request):
    isVerified = authenticate_user(request, "admin")
    print("admin verification", isVerified)
    return JsonResponse(isVerified is not None, safe=False)


# class AdminProfileDetailView(RetrieveAPIView):
#     serializer_class = AdminProfileSerializer

#     def get_queryset(self):
#         return User.objects.filter(is_admin=True, is_staff=True)
    

class AdminProfileDetailView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = AdminProfileSerializer(user)
        return Response(data=serializer.data)

