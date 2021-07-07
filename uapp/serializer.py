from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from .service import *

class DetailsUserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    user_email=serializers.EmailField(max_length=100)
    user_city=serializers.CharField(max_length=100)
    u_firstname=serializers.CharField(max_length=100)
    u_lastname=serializers.CharField(max_length=100)
   
    class Meta:
        model=DetailsUser
        fields=['username','password','user_email','user_city','u_firstname','u_lastname',]

    def Create(self,validate_data):
        return DetailsUser.objects.create(**validate_data)

    def validate(self,data):
        un=data.get('username')
        fn=data.get('u_firstname')
        ln=data.get('u_lastname')
        uc=data.get('user_city')
        up=data.get('password')
        email=data.get('user_email')
    

        passflag=passwordvalidate(up)
        if(not passflag):
            raise serializers.ValidationError("Your password must contain numerical values,at least one uppercase character,lower case characters and at least one special symbol.The password length must be atleast 8 character")
        
        if len(un)<4 or len(un)>10 :
            raise serializers.ValidationError('Length of this field should be greater than 4 characters and should be less than 10 characters ')
        if len(fn)<3 or len(fn)>10:
            raise serializers.ValidationError('Length of this field should be less than 10 characters and greater than 3 characters')
        if len(ln)<3 or len(ln)>10:
            raise serializers.ValidationError('Length of this field should be less than 10 characters and greater than 3 characters')
        
        result=checkeu(username,user_email)
        if len(result)==2:
            raise serializers.ValidationError('already taken')
        else:
            if result== 'e':
                raise serializers.ValidationError("Email exists")
            else:
                raise serializers.ValidationError("username is taken")      
        return data


 
class UserchatSerializer(serializers.ModelSerializer):     
    username=serializers.CharField(max_length=20)
    otherperson_username=serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model=ChatsUser
        fields=['username','otherperson_username']

        



