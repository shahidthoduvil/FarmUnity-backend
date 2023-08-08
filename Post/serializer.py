from .models import *
from rest_framework import serializers



class PostSerializer(serializers.Serializer):
     class Meta:

        models=Post
        fields='__all__'

class CommentSerializer(serializers.Serializer):
    class Meta:
        models=Comments
        fields='__all__'
    
        