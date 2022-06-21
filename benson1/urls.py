from django.urls import path
from django.contrib.auth import views as auth_views
from benson1.auth_views import DoctorRegView,DoctorLoginView,PatientRegView,PatientLoginView
from benson1.forms import DoctorLoginForm,PatientLoginForm


urlpatterns = [
	path('doc/register/',DoctorRegView.as_view(),name='doc-register'),
    path('doc/login/',DoctorLoginView.as_view(redirect_authenticated_user=True,template_name='auth/doctor_login.html',authentication_form=DoctorLoginForm),name='doctor-login'),
    path('doc/logout/',auth_views.LogoutView.as_view(template_name='auth/doctor_login.html'),name='doctor-logout'),
	path('user/register/',PatientRegView.as_view(),name='patient-register'),
    path('user/login/',PatientLoginView.as_view(redirect_authenticated_user=True,template_name='auth/patient_login.html',authentication_form=PatientLoginForm),name='patient-login'),
    path('user/logout/',auth_views.LogoutView.as_view(template_name='auth/patient_login.html'),name='patient-logout'),
]