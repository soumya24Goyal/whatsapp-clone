from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .serializer import *
import datetime
from .otp_gen import * 
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
from .service import *
from .task import *
from .chat import *
from ratelimit.decorators import ratelimit






class GETUser(APIView):
    def get(self,request):
        try:
            k = request.query_params["id"]
            result=DetailsUser.objects.get(k=id,is_deleted=False)
        except:
                return Response({"result":"INVALID ID"},status=status.HTTP_404_NOT_FOUND)
                serializer=DetailsUser(request)
                data={}
                data["username"]=result.username
                data["u_firstname"]=result.u_firstname
                data["u_lastname"]=result.u_lastname
                
                data["user_email"]=result.user_email
                data["user_city"]=result.user_city
                return Response(data=data,status=status.HTTP_200_OK)

class PUTUser(APIView):
    def put(self,request):
        try:
            k = request.query_params["id"]
            result=DetailsUser.objects.get(k=id)
        except:
            return Response({"result":"INVALID ID"},status=status.HTTP_404_NOT_FOUND)
            serializer=DetailsUserSerializer(result,data=request.data)
            if serializer.is_valid():
                serializer.save()    
                return Response(serializer.data)
            return Response({"result":"INVALID DATA"},status=status.HTTP_400_BAD_REQUEST)

        
                

    def patch(self,request):
        try:
            k=request.query_params["id"]
            result=DetailsUser.objects.get(id=k)
        except:
            return Response({"result":"ID NOT FOUND"},status=status.HTTP_404_NOT_FOUND)
            data = request.data
            result.username = data.get("username",result.username)
            result.user_email=data.get("user_email",result.user_email)
            result.user_city=data.get("user_city",result.user_city)
            result.u_firstname=data.get("u_firstname",result.u_firstname)
            result.u_lastname=data.get("u_lastname",result.u_lastname)
            result.password=data.get("password",result.password)
            
            
            result.save()
            serializer=DetailsUserSerializer(result)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class DeleteUser(APIView):
    def UserDelete(self,request):
        try:
            k=request.query_params["id"]
            result=DetailsUser.objects.get(k=id)
            if result.is_deleted:
                 return Response({"result":"Account NOT EXISTS"})
        except:
            return Response({"result":"ID NOT FOUND"},status=status.HTTP_404_NOT_FOUND)
           
            result.is_deleted='True'
            result.deleted_at=datetime.datetime.now()
            result.save()
            data={}
            data["success"]="Delete is successful"
            
            data["Failed"]="Delete is Failed"
            return Response(data=data)
    





class PostUser(APIView):
    def post(self,request):
        newinfo=DetailsUser()
        newpassword=hash_password(request.data['password'])
        serializer=DetailsUserSerializer(newinfo,data=request.data)
        name=request.data.get('username')
        result=get_user(name)
        if result is not None:
            return Response({'result':'Already exists'})
        else:
            if serializer.is_valid(raise_exception=True):
                ChatsUser.objects.create(username=name,otherperson_username=[ ])
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'result':"FAILED TO CREATE ENTRY"})
            





class OTPGenerate(APIView):
    #This api is to generate OTP .
    @ratelimit(rate='10/m')
    def post(self,request):
        email=request.query_params['email']
        result=checkeu(email)
        
        if result is None:
            return Response({'result':'Email NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        else:
            otp=GenerateOtp()
            send_email.delay(email,otp)
            key= email
            value=otp
            cache.set(key,value,300)
            return Response({'Result': ' Email send '})
       
class validateOtp(APIView):
    #This api is to verify otp.
    
    def post(self,request):
        result=checkeu(request)
        if result is None:
            return Response({'result':'Email NOT EXIST'},status=status.HTTP_404_NOT_FOUND)
        else:
            email=request.query_params['email']
            otp=request.data.get('otp')
            if otp is None:
                return Response({'result': 'OTP required'},status=status.HTTP_406_NOT_ACCEPTABLE)
            vldotp=validOtp(email,otp)
            if vldotp:
                acesstoken= MyTokenObtainPairSerializer()
                Acesst=acesstoken.get_token(result)
                return Response({'result':Acesst},status=status.HTTP_200_OK)
            else:
                return Response({'result':'wrong otp'})

#request.data.get('username'
        
class Chatapp(APIView):
    def post(self,request):
        cname=request.data.get('username')
        cn=get_user(cname) 
        cuser=request.data.get('otherperson_username')
        usr=get_user(cuser)
        if cn is None:
            return Response({'result':' Does not exist' })
        if usr is None:
            return Response({'result':'username does not exist' })
        else:
            result=is_connect(cn.username,usr.username)
            if result:
                return Response({'result':"Connection Already exists"})
            else:
                chatid= do_connect(cn,usr)
                Createchat(cn,usr,chatid)
                return Response({'result':"connected"})
            

