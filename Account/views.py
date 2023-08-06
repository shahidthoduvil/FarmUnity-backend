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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serilizer import UserProfileSerializer, AccountSerilizer,OccupationSerilizer,CategorySerilizer,UserSerializer
from .models import User, Address, Category, Occupation


from .models import *

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from .serilizer import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter
from .permision import IsAuthenticatedWithToken




from django.contrib.auth import authenticate

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
    def post(self,request):
        email=request.data.get('email')
        print(request.data)

        serializer=UserRegister(data=request.data)


        if serializer.is_valid(raise_exception=True):
            
            user= serializer.save()
    

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
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_admin'] = user.is_admin

        return token
    
# generate a token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




# google login 

class GoogleAuthentication(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not User.objects.filter(email=email).exists():
            serializer = GoogleAuthSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):

                user = serializer.save()
                user.is_active = True
                user.set_password(password)
                user.save()
# 
        user = authenticate(request, email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_tokens(user)
            response = {
                'msg': "Login successfull",
                'token': tokens,
                'status': 200,
                'user': {
                    'user_id': user.id,
                    'email': user.email,
                    'is_active': user.is_active,
                   
                },
            }
            return Response(data=response, status=status.HTTP_200_OK)

        return Response(data={'msg': 'Login Failed','status':400 })

#for validating email and senting reseting  mail to the user

class ForgotPasswordView(APIView):
    def post(self, request:Response):
        print('Function Called')

        email = request.data['email']
        print(email)
        if User.objects.filter(email=email).exists:
            user = User.objects.get(email=email)

            current_site=get_current_site(request)
            mail_subject = 'Reset your password'
            message=render_to_string('Reset_password_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            return Response({'msg':'Please Reset Password In The Link', 'user_id':user.id})
        else:
            return Response({"message": "Please Reset Password in the link"}, status=status.HTTP_400_BAD_REQUEST)

#for check for the user and directing to password reseting page

@api_view(['GET'])
def ResetPassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        return HttpResponseRedirect('http://localhost:3000/reset-password')
    else:
        return Response({'message':'Forgot password mail sented Success'}) 


#for reseting the the password

class ResetPasswordView(APIView):
    def post(self, request):
        str_user_id = request.data.get('user_id')
        password = request.data.get('password')

        if str_user_id is not None and password:
            try:
                user_id = int(str_user_id)
                user = User.objects.get(pk=user_id)
                user.set_password(password)
                user.save()
                return Response({'message': 'Password Updated successfully'})
            except (ValueError, User.DoesNotExist):
                return Response({'message': 'Invalid user ID'})
        else:
            

            return HttpResponseRedirect('http://localhost:3000/reset-password')
        

class ListUserview(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(is_admin=False, is_staff=False).order_by('-id')
    
    
class AdminSearchUser(ListCreateAPIView):
     serializer_class = UserSerializer
     filter_backends = [SearchFilter]
     queryset = User.objects.filter(is_admin=False, is_staff=False)
     search_fields = ['username']  




# for blocking  a user 

class BlockUser(APIView):
    def patch(self,request,id):
        try:
            user=User.objects.get(id=id)
            print(user,'user')
            user.is_active=not user.is_active
            user.save()
            return Response({'msg':"Blocked successfully"})
        except user.DoesNotExist:
            return Response({'msg':"User not found"})
        except Exception as e:
            return Response({'msg':str(e)})
            
       
        

# get User Details


class GetUserDetails(APIView):



    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_address = Address.objects.get(user=user)
        print('idjkdlfk',user.Occup)
        ocup_instance=Occupation.objects.get(id=user.Occup.id)
        print('Occup_instance',ocup_instance)
        category=ocup_instance.Cat.Category_name
        print('ffafalflafla',category)
      


        serializer = UserSerializer(user)
        occup_serializer = OccupationSerilizer(ocup_instance)
        user_serializer = AccountSerilizer(user_address)

        response_data = {
            'user': serializer.data,
            'user_address': user_serializer.data,
            'user_occupation': occup_serializer.data,
            'category': category,

        }
        return Response(response_data)
    

class  userProfileSet1(UpdateAPIView):
  queryset=User.objects.all()
  serializer_class=UserProfileSerializer
  lookup_field='id'

class userProfileSet2(ListCreateAPIView):

  queryset=Address.objects.all()
  serializer_class=AccountSerilizer    