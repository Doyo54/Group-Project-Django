from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from benson1.auth_forms import DoctorRegForm,PatientRegForm,DoctorLoginForm,PatientLoginForm
from django.views import View


# auth views
class DoctorRegView(View):
	form_class = DoctorRegForm
	initial = {'key': 'value'}
	template_name = 'auth/doc_signup.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(to='/doc/submit/details/')

		return super(DoctorRegView, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		doc_reg_form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {"doc_reg_form": doc_reg_form})

	def post(self, request, *args, **kwargs):
		doc_reg_form = self.form_class(request.POST)
		if doc_reg_form.is_valid():
			doc_reg_form.save()

			username = doc_reg_form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')

			return redirect(to='/doc/submit/details/')
		return render(request, self.template_name, {"doc_reg_form": doc_reg_form})


class DoctorLoginView(LoginView):
	form_class = DoctorLoginForm

	def form_valid(self, doc_login_form):
		remember_me = doc_login_form.cleaned_data.get('remember_me')
		if not remember_me:
			self.request.session.set_expiry(0)
			self.request.session.modified = True
		return super(DoctorLoginView, self).form_valid(doc_login_form)


class PatientRegView(View):
	form_class = PatientRegForm
	initial = {'key': 'value'}
	template_name = 'auth/patient_signup.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(to='/user/profile/')

		return super(PatientRegView, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		patient_reg_form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {"patient_reg_form": patient_reg_form})

	def post(self, request, *args, **kwargs):
		patient_reg_form = self.form_class(request.POST)
		if patient_reg_form.is_valid():
			patient_reg_form.save()

			username = patient_reg_form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')

			return redirect(to='/user/profile/')
		return render(request, self.template_name, {"patient_reg_form": patient_reg_form})


class PatientLoginView(LoginView):
	form_class = PatientLoginForm

	def form_valid(self, patient_login_form):
		remember_me = patient_login_form.cleaned_data.get('remember_me')
		if not remember_me:
			self.request.session.set_expiry(0)
			self.request.session.modified = True
		return super(PatientLoginView, self).form_valid(patient_login_form)
