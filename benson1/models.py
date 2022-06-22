from django.contrib.auth.models import AbstractBaseUser,User, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


# auth models--overriding django's registration
class DoctorAccountManager(BaseUserManager):
    def new_doctor(self,email,username,first_name,last_name,specialty,license_number,location,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        doctor = self.model(email=email,username=username,first_name=first_name,last_name=last_name,specialty=specialty,license_number=license_number,location=location,**other_fields)
        doctor.set_password(password)
        doctor.save()
        return doctor


class Doctor(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'),max_length=150,unique=True,default='')
    username = models.CharField(_('Username'),max_length=150,unique=True,default='')
    first_name = models.CharField(max_length=150,default='')
    last_name = models.CharField(max_length=150,default='')
    specialty = models.CharField(max_length=100,default='')
    license_number = models.PositiveIntegerField(default=000000,validators=[MinValueValidator(0),MaxValueValidator(999999)])
    location = models.CharField(max_length=100,default='')
    reg_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = DoctorAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name','specialty','license_number',]

    def __str_(self):
        return self.first_name


class PatientAccountManager(BaseUserManager):
    def new_patient(self,email,username,first_name,last_name,age,sex,location,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        patient = self.model(email=email,username=username,first_name=first_name,last_name=last_name,age=age,sex=sex,location=location,**other_fields)
        patient.set_password(password)
        patient.save()
        return patient

