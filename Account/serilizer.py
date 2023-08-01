from rest_framework import serializers
from.models import *



    




class UpdateUserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['pic','cover','username']



class AccountSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields= '__all__'
    

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
        fields=['first_name','last_name','username','email','phone_number','password']
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












class UserSerializer(serializers.ModelSerializer):



    Occup = OccupationSerilizer()
    Cat = CategorySerilizer(source='Occup.Cat')

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