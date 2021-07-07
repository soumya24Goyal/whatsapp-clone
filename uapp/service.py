from .models import *
import crypt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



def passwordvalidate(password):
    num = False
    upper = False
    lower = False
    if (len(password) <=5 or len(password) >17 ): return False

    for char in range (0,len(password)):
        if ( num  and upper and lower ): return True
        if (not(num) and password[char].isdigit()): 
            num = True
            continue
        if (not(lower) and password[char].islower()):
            lower = True
            continue
        if (not(upper) and password[char].isupper()):
            upper = True
            continue
    return False

def hash_password(text):
    hash=crypt.crypt(text)
    return hash

def checkeu(user_name,user_email):
    flag=""
    try:
       result = DetailsUser.objects.get(username=user_name,is_deleted=False)
       if result.username == user_name :
            flag = 'u'
       if result.email == user_email :
            flag = flag+'e'
       return flag
    except:
       return flag

def get_user(request):
    try:
        result = DetailsUser.objects.get(username=request)
        return result
    except:
        result=None
        return result

def do_connect(user1,user2):
    out1=ChatsUser.objects.get(username=user1.username)
    out1.otherperson_username.append(user2.username)
    out1.save()
    out2=ChatsUser.objects.get(username=user2.username)
    out2.otherperson_username.append(user1.username)
    out2.save()
    id=[out1.id,out2.id]
    return id

    




def is_connect(user1,user2):
    try:
        result=ChatsUser.objects.get(username=user1 , otherperson_username__contains=[user2])
        return True
    except:
        return False

def check_id(id):
    try:
        result=ChatsUser.objects.get(id=id)
        return result
    except:
        result=None
        return result
        
        

    
def checkname(name):
    try:
        result=ChatsUser.objects.get(otherperson_username=name)
        return result
    except:
        result=None
        return result
def check_name(other):
    try:
        result=ChatsUser.objects.get(usename=other)
        return result
    except:
        result=None
        return result
    


        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        data={}
        data['refresh token']=str(token)
        data['access token']=str(token.access_token)
        return data

