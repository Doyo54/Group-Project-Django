from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from benson1.models import AllUsers
from django import forms


class DoctorRegForm(RegistrationForm):
	class Meta:
		model = AllUsers
		fields = ('username','email','first_name','last_name','specialty','license_number','location')


class DoctorLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(required=False)

	class Meta:
		model = AllUsers
		fields = ('username', 'license_number',)


class PatientRegForm(RegistrationForm):
	class Meta:
		model = AllUsers
		fields = ('username','email','first_name','last_name','age','sex','location')


class PatientLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(required=False)

	class Meta:
		model = AllUsers
		fields = ('username',)
