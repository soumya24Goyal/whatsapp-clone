from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import (BaseUserManager,
                                        PermissionsMixin)
from .base import BaseModel
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import ArrayField


class DetailsUser(AbstractBaseUser,PermissionsMixin,BaseModel):
    class Meta:
        db_table='myuser'
        

    username=models.CharField(max_length=100,null=True,unique=True)
    user_email=models.EmailField(max_length=100,null=False,unique=True)
    user_city=models.TextField(max_length=100,null=False)
    email_verified=models.BooleanField(default=False)
    u_firstname=models.CharField(max_length=100,null=True)
    u_lastname=models.CharField(max_length=100,null=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['username','user_email']
   

class ChatsUser(models.Model):
    class Meta:
        db_table='chats'
    username=models.CharField(max_length=20,null=False)  
    otherperson_username=ArrayField(models.CharField(max_length=20),null=True)
    
   

    
# Create your models here.
