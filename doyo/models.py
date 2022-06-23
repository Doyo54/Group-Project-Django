from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts', null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
  

    @classmethod
    def get_Profile(cls, user):
        profile = Post.objects.filter(user__user=user).all()
        return profile

    def save_post(self):
        self.save()
    
    @classmethod
    def update_post(cls, id, value):
        cls.objects.filter(id=id).update(title=value)

    @classmethod
    def update_caption(cls, id, value):
        cls.objects.filter(id=id).update(description=value)

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Post'

