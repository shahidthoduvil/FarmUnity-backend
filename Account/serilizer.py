from rest_framework import serializers
from.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self,validate_data):
        password=validate_data.pop('password',None)
        instance=self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'
    
class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

    
class OccupationSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Occupation
        fields='__all__'