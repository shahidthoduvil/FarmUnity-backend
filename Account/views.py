from django.shortcuts import render
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

from .models import *

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.




#

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh'
    ]
    return Response(routes)


# user registration  and sending activate email


class RegisterView(APIView):
    print('Register View')
    def post(self,request):
        email=request.data.get('email')
        print(request.data)

        serializer=UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user  = serializer.save()

            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            mail_subject = 'Please activate your account'

            message= render_to_string('account_verify_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'usename': urlsafe_base64_encode(force_bytes(user.username))
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return Response({'msg':'Registration Success'})
        
        return Response({'msg':'Registration Failed'})

           
#for activating user  and directing to login page  
@api_view(['GET'])
def Activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        print('saved')

        return HttpResponseRedirect('http://localhost:3000/login')



# customizing jwt token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['is_staff'] = user.is_staff
        token['is_admin'] = user.is_superadmin 

        return token
    
# generate a token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
