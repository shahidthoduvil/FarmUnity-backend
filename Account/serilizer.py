from rest_framework import serializers
from .models import *

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['pic','cover','username']



class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        instance = Address.objects.create(**validated_data)
        user_instance = instance.user
        user_instance.is_setup_complete = True
        user_instance.save() 
        return instance
    

class CategorySerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'

    
class OccupationSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Occupation
        fields='__all__'

class GoogleAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['pic','cover','Occup','cat']




class UserRegister(serializers.ModelSerializer):
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





class CategorySerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'

    
class OccupationSerilizer(serializers.ModelSerializer):

    class Meta:
        model=Occupation
        fields='__all__'






class UserSerializer(serializers.ModelSerializer):



    Occup = OccupationSerilizer()
    cat = CategorySerilizer()

    class Meta:
        model=User
        fields='__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }



class getProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','pic','cover','phone_number','id']


