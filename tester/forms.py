from tester.models import Patient,Doctor,Dummy
from django import forms


class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ('age','sex','weight','location','existing_medical_conditions','allergies','current_medication')


class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = ('specialty','medical_license','licensed_by','national_id','field_of_experience','years_of_practice')


