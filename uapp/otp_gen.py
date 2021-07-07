import random,math
from django.core.cache import cache
from django.conf import settings





def GenerateOtp():
    digits="0123456789"
    OTP= ""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP

def validOtp(key,value):
    otp=cache.get(key)
    if otp is None:
        return False
    else:
        if(otp==value):
            cache.delete(key)
            return True
        else: 
            return False



   