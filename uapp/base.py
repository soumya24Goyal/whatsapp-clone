from django.db import models
class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    deleted_at=models.DateTimeField(null=True,blank=True)
    is_deleted=models.BooleanField(default=False)
    
