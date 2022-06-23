from django.db import models

from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# auth models--overriding django's registration
class AllUsersAccountManager(BaseUserManager):
    def new_user(self,email,username,first_name,last_name,license_number,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        new_user = self.model(email=email,username=username,first_name=first_name,last_name=last_name,license_number=license_number,**other_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user


class AllUsers(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'),max_length=150,unique=True,default='')
    username = models.CharField(_('Username'),max_length=60,unique=True,default='')
    first_name = models.CharField(max_length=150,unique=False,default='')
    last_name = models.CharField(max_length=150,unique=False,default='')
    license_no = models.PositiveIntegerField(default=123456,validators=[MinValueValidator(10000),MaxValueValidator(999999)])
    reg_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AllUsersAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','license_no']

    def __str_(self):
        return self.email


class Doctor(models.Model):
    doctor = models.ForeignKey(AllUsers, on_delete=models.DO_NOTHING, null=True)
    what_you_do_in_a_few_words = models.CharField(max_length=200, default='')
    photo_url = models.ImageField(upload_to='images/',default='default.png')
    specialty = models.CharField(max_length=100, default='')
    medical_license = models.ImageField(upload_to='images/',default='default.png')
    licensed_by = models.CharField(max_length=60, default='')
    national_id = models.PositiveIntegerField(default=12345670,
                                              validators=[MinValueValidator(10000000), MaxValueValidator(99999999)])
    field_of_experience = models.CharField(max_length=100, default='')
    years_of_practice = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(50)])


class Patient(models.Model):
    patient = models.ForeignKey(AllUsers, on_delete=models.DO_NOTHING, null=True)
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(90)])
    CHOICES = (('M', 'Male'), ('F', 'Female'), ('N', 'Prefer not to say'))
    sex = models.CharField(max_length=100, choices=CHOICES, null=True)
    weight = models.PositiveIntegerField(default=30, validators=[MinValueValidator(10), MaxValueValidator(500)])
    location = models.CharField(max_length=60, default='')
    existing_medical_conditions = models.CharField(max_length=60, null=True)
    allergies = models.CharField(max_length=60,null=True)
    current_medication = models.CharField(max_length=60,null=True)


class Room(models.Model):
    name = models.CharField(max_length=500)


class Chat(models.Model):
    message = models.CharField(max_length=10000, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(AllUsers, on_delete=models.DO_NOTHING, null=True)
    room = models.CharField(max_length=500, null=True)


class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Dummy(models.Model):
    name = models.CharField(max_length=200)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(AllUsers, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/',default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'
    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile_picture=value)
    def save_profile(self):
        self.name
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts', null=True)
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
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Post'