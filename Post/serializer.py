from .models import *
from rest_framework import serializers
from Account.serilizer import *
from rest_framework.serializers import SerializerMethodField



class PostSerializer(serializers.ModelSerializer):
     
    user = UserSerializer() 
    is_liked = SerializerMethodField()

  
    class Meta:
        model=Post
        fields=['id', 'title', 'description', 'image', 'date', 'user','comment_count','like_count','Location','is_liked']

    
    def get_is_liked(self,obj):
        user = User.objects.get(id=self.context.get('user_id'))  
        print(Like.objects.filter(user=user,post=obj))
        return Like.objects.filter(user=user,post=obj).exists()
    

class PostUserSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    is_liked = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'date', 'user', 'comment_count', 'like_count', 'Location', 'is_liked']

    def get_is_liked(self, obj):
        username = self.context.get('username')
        if username is not None:
            try:
                user = User.objects.get(username=username)
                return Like.objects.filter(user=user, post=obj).exists()
            except User.DoesNotExist:
                return False
        return False


class CommentSerializer(serializers.ModelSerializer):
    userdetails=serializers.SerializerMethodField()
    class Meta:
        model=Comments
        fields='__all__'
        extra_kwargs={
            'user':{'write_only':True}
        }
    def get_userdetails(self,obj):
        userdetails = {}
        userdetails.update(username=UserSerializer(obj.user).data.get('username'))
        userdetails.update(pic=UserSerializer(obj.user).data.get('pic'))
        return userdetails
    

class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields='__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields="__all__"