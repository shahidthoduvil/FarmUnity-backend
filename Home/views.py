from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

class getBannerLIst(APIView):
    def get(self,request):
        banner=Banner.objects.all()
        serializer=BannerListSerializer(banner,many=True)
        return Response(serializer.data)
    
class BannerCreateView(APIView):
    def post(self, request):
        serializer = BannerListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['DELETE'])
def bannerDelete(request, pk):
    banner = Banner.objects.get(id=pk)
    banner.delete()
    return Response('User deleted')

 
class getQuoteLIst(APIView):
    def get(self,request):
        quote=Quote.objects.all()
        serializer=QuoteListSerializer(quote,many=True)
        return Response(serializer.data)
    
class QuoteCreateView(APIView):
    def post(self,request):
        serializer=QuoteListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
 
class QuoteUpdate(APIView):
    def put(self, request, pk):
        try:
            quote = Quote.objects.get(id=pk)
        except Quote.DoesNotExist:
            return Response({"error": "Quote not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuoteListSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def quoteDelete(request, pk):
    banner = Quote.objects.get(id=pk)
    banner.delete()
    return Response('User deleted')

    
class getMemberLIst(APIView):
    def get(self,request):
        member=Member.objects.all()
        serializer=MemberListSerializer(member,many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
def memberDelete(request, pk):
    banner = Member.objects.get(id=pk)
    banner.delete()
    return Response('User deleted')


class MemberCreateView(APIView):
    def post(self,request):
        serializer=MemberListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
