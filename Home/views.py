from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


# Create your views here.

class getBannerLIst(APIView):
    def get(self,request):
        banner=Banner.objects.all()
        serializer=BannerListSerializer(banner,many=True)
        return Response(serializer.data)
    
    
class getQuoteLIst(APIView):
    def get(self,request):
        quote=Quote.objects.all()
        serializer=QuoteListSerializer(quote,many=True)
        return Response(serializer.data)
    
class getMemberLIst(APIView):
    def get(self,request):
        member=Member.objects.all()
        serializer=MemberListSerializer(member,many=True)
        return Response(serializer.data)
