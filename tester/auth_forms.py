from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from doyo.models import AllUsers
from django import forms


class DoctorRegForm(RegistrationForm):
	class Meta:
		model = AllUsers
		fields = ('username','first_name','last_name','email','license_no',)


class PatientRegForm(RegistrationForm):
	class Meta:
		model = AllUsers
		fields = ('username','first_name','last_name','email',)


class LoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(required=False)

	class Meta:
		model = AllUsers
		fields = ('username',)