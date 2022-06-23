from tester.models import Patient,Doctor,Dummy 
from django import forms


class PatientForm(forms.Form):
	class Meta:
		model = Patient
		fields = ('age','sex','weight','location','existing_medical_conditions','allergies','current_medication')


class DoctorForm(forms.Form):
	class Meta:
		model = Doctor
		fields = ('specialty','medical_license','licensed_by','national_id','field_of_experience','years_of_experience')


from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from tester.models import AllUsers
from django import forms


class DoctorRegForm(RegistrationForm):
	class Meta:
		model = AllUsers
		fields = ('username','email','license_no',)


class DoctorLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(required=False)

	class Meta:
		model = AllUsers
		fields = ('username', 'license_no',)


class PatientRegForm(RegistrationForm):
	class Meta:
		model = AllUsers
		fields = ('username','email',)


class PatientLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(required=False)

	class Meta:
		model = AllUsers
		fields = ('username',)

class Dummy(forms.Form):
	class Meta:
		model = Dummy
		fields = ('name')
