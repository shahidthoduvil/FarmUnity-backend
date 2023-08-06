from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
# Create your views here.

class getBannerLIst(APIView):
    def get(self,request):
        banner=Banner.objects.filter(is_list=True)
        serializer=BannerListSerializer(banner,many=True)
        return Response(serializer.data)
    

class getAdminBannerLIst(APIView):
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



class ListUnlistBanner(APIView):
   def patch(self, request, pk):
        try:
            banner = Banner.objects.get(id=pk)
        except Banner.DoesNotExist:
            return Response({"error": "Quote not found"}, status=status.HTTP_404_NOT_FOUND)

        is_list = request.data.get("is_list", None)
        if is_list is None:
            return Response({"error": "is_list parameter not provided"}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(is_list, bool):
            return Response({"error": "is_list parameter should be a boolean value"}, status=status.HTTP_400_BAD_REQUEST)

        banner.is_list = is_list
        banner.save()

        serializer = QuoteListSerializer(banner)
        return Response(serializer.data)
   


class BannerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Banner.objects.all()
    serializer_class=BannerListSerializer

@api_view(['DELETE'])
def bannerDelete(request, pk):
    banner = Banner.objects.get(id=pk)
    banner.delete()
    return Response('User deleted')

 
class getQuoteLIst(APIView):
    def get(self,request):
        quote=Quote.objects.filter(is_list=True)
        serializer=QuoteListSerializer(quote,many=True)
        return Response(serializer.data)
    

class getAdminquote(APIView):
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

    def get(self,request,pk):
        try:
            quote = Quote.objects.get(id=pk)
        except Quote.DoesNotExist:
            return Response({"error": "Quote not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuoteListSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 
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

    

class ListUnlist(APIView):
   def patch(self, request, pk):
        try:
            quote = Quote.objects.get(id=pk)
        except Quote.DoesNotExist:
            return Response({"error": "Quote not found"}, status=status.HTTP_404_NOT_FOUND)

        is_list = request.data.get("is_list", None)
        if is_list is None:
            return Response({"error": "is_list parameter not provided"}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(is_list, bool):
            return Response({"error": "is_list parameter should be a boolean value"}, status=status.HTTP_400_BAD_REQUEST)

        quote.is_list = is_list
        quote.save()

        serializer = QuoteListSerializer(quote)
        return Response(serializer.data)
  


@api_view(['DELETE'])
def quoteDelete(request, pk):
    banner = Quote.objects.get(id=pk)
    banner.delete()
    return Response('User deleted')

    
class getMemberLIst(APIView):
    def get(self,request):
        member=Member.objects.filter(is_list=True)
        serializer=MemberListSerializer(member,many=True)
        return Response(serializer.data)




class getAdminMember(APIView):
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

class ListUnlistMember(APIView):
   def patch(self, request, pk):
        try:
            member = Member.objects.get(id=pk)
        except Member.DoesNotExist:
            return Response({"error": "Quote not found"}, status=status.HTTP_404_NOT_FOUND)

        is_list = request.data.get("is_list", None)
        if is_list is None:
            return Response({"error": "is_list parameter not provided"}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(is_list, bool):
            return Response({"error": "is_list parameter should be a boolean value"}, status=status.HTTP_400_BAD_REQUEST)

        member.is_list = is_list
        member.save()

    
        # if not is_list and member.category:
        #     from django.contrib.auth import get_user_model
        #     User = get_user_model()
        #     associated_users = User.objects.filter(cat=member.category, is_active=True)
        #     for user in associated_users:
        #         user.is_active = False
        #         user.save()
        serializer = QuoteListSerializer(member)
        return Response(serializer.data)


class MemberEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Member.objects.all()
    serializer_class=MemberListSerializer