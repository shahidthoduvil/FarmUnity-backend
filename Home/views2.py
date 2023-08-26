from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView,CreateAPIView,DestroyAPIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from Account.serilizer import *
from django.db.models import Q
from django.contrib.auth import get_user_model
from Account.permision import IsAuthenticatedWithToken
User = get_user_model()

class UserByCategoryView(APIView):
    permission_classes = [IsAuthenticatedWithToken]

    def get(self, request, categoryName):
        try:
            users = User.objects.filter(Occup__Cat__Category_name=categoryName).exclude(id=request.user.id)

            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": f"Error fetching users by category. {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchUsersByCategory(APIView):
    def get(self, request, categoryName):
        try:
            search_query = request.query_params.get('q', '')
            users = User.objects.filter(
                Q(Occup__Cat__Category_name=categoryName) &
    (Q(Occup__titile__icontains=search_query) |
     Q(username__icontains=search_query) |
     Q(first_name__icontains=search_query))
)
            
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": f"Error searching users by category and occupation. {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class AutoSuggestUsers(APIView):
    def get(self, request, categoryName):
        try:
            search_query = request.query_params.get('q', '')
            suggestions = User.objects.filter(
             Q(Occup__Cat__Category_name=categoryName) &
                Q(Occup__titile__icontains=search_query) |
                Q(username__icontains=search_query) |
                Q(first_name__icontains=search_query)
            ).values('id', 'username', 'first_name', 'last_name','Occup__titile')
            return Response(suggestions)
        except Exception as e:
            return Response({"message": f"Error fetching auto-suggestions. {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# class ProfileView(APIView):
#     def get(self, request, username):
#         try:
#             user = User.objects.get(username=username)
#             serializer =  getProfileSerializer(user)
#             return Response({'user': serializer.data}, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class GetUserinfo(APIView):

    def get(self, request, username):
        user = User.objects.get(username=username)
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
    


# class AllReviewsListView(APIView):
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



class User1ReviewsListView(APIView):
    def get(self, request, user1_id):
        reviews = Review.objects.filter(user1=user1_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class User1Reviews(APIView):
    def get(self, request, username):
        reviews = Review.objects.filter(user1__username=username)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class User1CreateReviews(CreateAPIView):
    serializer_class =  CreateReviewSerializer

    def perform_create(self, serializer):
        username=self.request.data.get('username')
        user=User.objects.get(username=username)
        serializer.save(user1=user)
        return super().perform_create(serializer)



# class ReviewDeleteView(APIView):
#     def delete(self, request, review_id):
#         try:
#             review = Review.objects.get(pk=review_id)
#         except Review.DoesNotExist:
#             return Response({"error": "Review not found."}, status=status.HTTP_404_NOT_FOUND)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewDeleteView(DestroyAPIView):
    serializer_class=ReviewSerializer
    queryset = Review.objects.all()
    lookup_field='id'
  
