from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from tester.auth_views import DoctorRegView,AllUsersLoginView,PatientRegView
from tester.auth_forms import LoginForm
from tester.views import home,doc,doc_profile,chat_home,chat,check,user,user_profile
from tester import views

urlpatterns = [
	path('home/',home,name='home'),
	path('',chat_home,name='index'),
	path('chat/<str:room_name>/',chat,name='chat'),
	path('check',check,name='check'),
	path('doc/signup/',DoctorRegView.as_view(),name='doc-signup'),
	path('doc/submit/details/',doc,name='doc-details'),
	path('user/submit/details/',user,name='user-details'),
	re_path(r'^doc/profile/(?P<id>\w+)/',doc_profile,name='doc-profile'),
	path('user/profile/',user_profile,name='user-profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name='auth/logout.html'),name='logout'),
	path('user/signup/',PatientRegView.as_view(),name='user-signup'),
    path('login/',AllUsersLoginView.as_view(redirect_authenticated_user=True,template_name='auth/login.html',authentication_form=LoginForm),name='login'),
	path('video/', views.lobby),	
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]