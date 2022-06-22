from django.db import models
from django.contrib.auth.models import User

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