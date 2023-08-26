from .models import *
from rest_framework import serializers
from Account.serilizer import *
from rest_framework.serializers import SerializerMethodField




class QuestionSerializer(serializers.ModelSerializer):
    user=UserSerializer()
   
    class Meta:
        model=Question
        fields='__all__'


class SolutionSerializer(serializers.ModelSerializer):

    user=UserSerializer()
    
    class Meta:
        model=Solution
        fields='__all__'


class CreateQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Question
        fields='__all__'

class createSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Solution
        fields='__all__'


class NotificationSerializer(serializers.ModelSerializer):
    user=AdminProfileSerializer()
    class Meta:
        model=Notification
        fields='__all__'

class CreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender_username=SerializerMethodField()

    class Meta:
        model=Messages
        fields=['message','sender_username']

    def get_sender_username(self,obj):
        return obj.sender.username

class ChatListSerializer(serializers.ModelSerializer):

    user_profile=SerializerMethodField
    username=SerializerMethodField

    class Meta:
        model=Messages
        fields=['user_profile','username']

    def get_username(self,obj):
        return obj
    
    def get_user_profile(self,obj):
        return UserProfileSerializer(User.objects.filter(user__username=obj).first()).data.get('pic')
    

