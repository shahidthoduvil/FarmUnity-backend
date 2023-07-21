from rest_framework import serializers
from .models import *



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

    