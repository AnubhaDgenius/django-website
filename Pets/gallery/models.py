from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
def validate_img(upload): 
      import os
      ext = os.path.splitext(upload.name)[1]
      if not ext in ['.jpg', ".png"]:
        raise ValidationError(u'File type not supported!')    
      if upload.size > 1024*500:
        raise ValidationError(u'File too big!')


class Notice(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    cr_date = models.DateField(auto_now=True)
    notice_details=models.FileField(upload_to = "doc\\", null=True, blank=True)
    def __str__(self):
        return self.subject

class Owner(models.Model):
    name = models.CharField(max_length=200, null=True)
    name_pet = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True) 
    breed=models.CharField(max_length=200, null=True)
    age_pet = models.IntegerField(default=1,)
    myimg=models.ImageField(upload_to = "images\\", validators=[validate_img], null=True)
    myimg_pet=models.ImageField(upload_to = "images\\", validators=[validate_img], null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Ques(models.Model):
    question = models.TextField(null=True) 
    answer = models.TextField(null=True) 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    notice=models.ForeignKey(Notice, on_delete=models.CASCADE)
    def __str__(self):
        return self.question    
    
