from django.urls import path
from django.contrib.auth import views as auth_views
from tester.auth_views import DoctorRegView,DoctorLoginView,PatientRegView
from tester.forms import DoctorLoginForm,PatientLoginForm
from tester.views import home,doc,doc_profile,chat_home,chat,check,user
from tester import views

urlpatterns = [
	path('home/',home,name='home'),
	path('',chat_home,name='index'),
	path('chat/<str:room_name>/',chat,name='chat'),
	path('check',check,name='check'),
	path('doc/register/',DoctorRegView.as_view(),name='doc-register'),
    path('doc/login/',DoctorLoginView.as_view(template_name='auth/login.html',authentication_form=DoctorLoginForm),name='doctor-login'),
	path('doc/submit/details/',doc,name='doc-details'),
	path('user/submit/details/',user,name='user-details'),
	path('doc/profile',doc_profile,name='doc-profile'),
    path('doc/logout/',auth_views.LogoutView.as_view(template_name='auth/login.html'),name='doctor-logout'),
	path('user/register/',PatientRegView.as_view(),name='patient-register'),
    # path('user/login/',PatientLoginView.as_view(template_name='auth/login.html',authentication_form=PatientLoginForm),name='patient-login'),
    path('user/logout/',auth_views.LogoutView.as_view(template_name='auth/patient_login.html'),name='patient-logout'),

	path('video/', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]