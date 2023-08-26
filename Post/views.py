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

# Create your views here.


    
# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     print(queryset,'fkjjfojsofjof')
#     serializer_class = PostSerializer

class PostList(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.select_related('user').all().order_by('-date')
    

class AddPostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer



class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer
    lookup_field='id'

    

class UserCommentsView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            print(post_id,'fjajfdld')
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_comments = Comments.objects.filter(post=post, user=request.user)
        serializer = CommentSerializer(user_comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PostCommentsView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        
        comments = Comments.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddCommentView(generics.CreateAPIView):
     queryset=Comments.objects.all()
     serializer_class = CommentSerializer



class UserPostList(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  
        return Post.objects.filter(user_id=user_id).order_by('-date')


class DeletePost(APIView):
    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.user_id == request.user.id:
                post.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "You are not authorized to delete this post."}, status=status.HTTP_403_FORBIDDEN)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        


class CommentDeleteView(DestroyAPIView):
    queryset =  Comments.objects.all()
    serializer_class = CommentSerializer
    lookup_field='id'


@api_view(['POST'])
def un_like_post(request):
    user_id = request.data.get('user')
    post_id = request.data.get('post')
    is_post_exist = Like.objects.filter(post__id=post_id,user__id=user_id).exists()
    if is_post_exist:
        post_like_instance = Like.objects.get(post__id=post_id,user__id=user_id)
        post_like_instance.delete()
        return Response(status=204)
    else:
        return Response(status=404, data={"message": "given post not found"})
    

class PostLikeView(ListCreateAPIView):
    serializer_class = LikeSerializer
    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Like.objects.filter(post__id=post_id)