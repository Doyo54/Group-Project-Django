from django.urls import path
from django.contrib.auth import views as auth_views
from benson1.auth_views import DoctorRegView,DoctorLoginView,PatientRegView,PatientLoginView
from benson1.auth_forms import DoctorLoginForm,PatientLoginForm
from benson1.views import home,doc,doc_profile


urlpatterns = [
	path('',home,name='home'),
	path('doc/register/',DoctorRegView.as_view(),name='doc-register'),
    path('doc/login/',DoctorLoginView.as_view(template_name='auth/doctor_login.html',authentication_form=DoctorLoginForm),name='doctor-login'),
	path('doc/submit/details/',doc,name='doc-details'),
	path('doc/profile',doc_profile,name='doc-profile'),
    path('doc/logout/',auth_views.LogoutView.as_view(template_name='auth/doctor_login.html'),name='doctor-logout'),
	path('user/register/',PatientRegView.as_view(),name='patient-register'),
    path('user/login/',PatientLoginView.as_view(template_name='auth/patient_login.html',authentication_form=PatientLoginForm),name='patient-login'),
    path('user/logout/',auth_views.LogoutView.as_view(template_name='auth/patient_login.html'),name='patient-logout'),
]