# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload = 'profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'

from django.db import models
