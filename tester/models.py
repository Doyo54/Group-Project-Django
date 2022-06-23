from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from django.db import models
from datetime import datetime


# auth models--overriding django's registration
class AllUsersAccountManager(BaseUserManager):
    def new_user(self,email,username,first_name,last_name,age,sex,specialty,license_number,location,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        new_user = self.model(email=email,username=username,first_name=first_name,last_name=last_name,age=age,sex=sex,specialty=specialty,license_number=license_number,location=location,**other_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user


class AllUsers(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'),max_length=150,unique=True,default='')
    username = models.CharField(_('Username'),max_length=150,unique=True,default='')
    license_no = models.PositiveIntegerField(default=12345670,validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    reg_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AllUsersAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str_(self):
        return self.email


class Doctor(models.Model):
    doctor = models.ForeignKey(AllUsers,on_delete=models.DO_NOTHING,null=True)
    specialty = models.CharField(max_length=100, default='')
    medical_license = CloudinaryField('image')
    licensed_by = models.CharField(max_length=60,default='')
    national_id = models.PositiveIntegerField(default=12345670,validators=[MinValueValidator(10000000),MaxValueValidator(99999999)])
    field_of_experience = models.CharField(max_length=100, default='')
    years_of_practice = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(50)])


class Patient(models.Model):
    patient = models.ForeignKey(AllUsers,on_delete=models.DO_NOTHING,null=True)
    age = models.PositiveIntegerField(default=18,validators=[MinValueValidator(18),MaxValueValidator(90)])
    CHOICES = (('M','Male'),('F','Female'),('N','Prefer not to say'))
    sex = models.CharField(max_length=100, default='',choices=CHOICES,null=True)
    weight = models.PositiveIntegerField(default=30,validators=[MinValueValidator(10),MaxValueValidator(500)])
    location = models.CharField(max_length=60, default='')
    existing_medical_conditions = models.CharField(max_length=60,null=True)
    allergies = models.CharField(max_length=60, default='',null=True)
    current_medication = models.CharField(max_length=60, default='',null=True)


class Room(models.Model):
	name = models.CharField(max_length=500)


class Chat(models.Model):
    message = models.CharField(max_length=10000,null=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.ForeignKey(AllUsers,on_delete=models.DO_NOTHING,null=True)
    room = models.CharField(max_length=500,null=True)

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Dummy(models.Model):
    name = models.CharField(max_length=200)