from rest_framework import serializers
from .models import *
from Account.serilizer import *



class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields='__all__'


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields='__all__'

class QuoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quote
        fields='__all__'

        
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    user1 = UserSerializer() 
 
    class Meta:
        model = Review
        fields = ['user', 'rate', 'message', 'user1','id']  

class CreateReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Review
        fields='__all__'
