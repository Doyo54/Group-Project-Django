from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from tester.models import Room,Chat
from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from tester.models import RoomMember,Doctor,Patient
from tester.forms import PatientForm,DoctorForm
import json
from tester.forms import Dummy
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	message = 'Hello, Africa'
	title = 'Home'
	return render(request, 'index.html',{"message":message,"title":title})


def doc(request):
	message = 'Just testing things for now'
	title = "Doc's details"
	form = Dummy
	if request.method == 'POST':
		docform = DoctorForm(request.POST)
		if docform.is_valid():
			print('valid!')
			specialty = docform.cleaned_data['specialty']
			medical_license = docform.cleaned_data['medical_license']
			licensed_by = docform.cleaned_data['licensed_by']
			doctor = Doctor(specialty=specialty,medical_license=medical_license,licensed_by=licensed_by,)
			# location.user = current_user
			doctor.save()
		return redirect('doc-profile')
	else:
		docform = DoctorForm()
	return render(request, 'doc/credentials.html',{"message":message,"title":title,"docform":docform,"form":form})

def user(request):
	message = 'Just testing things for now'
	title = "Patient's details"
	if request.method == 'POST':
		patientform = PatientForm(request.POST)
		if patientform.is_valid():
			print('valid!')
			age = patientform.cleaned_data['age']
			sex = patientform.cleaned_data['sex']
			weight = patientform.cleaned_data['weight']
			location = patientform.cleaned_data['location']
			existing_medical_conditions = patientform.cleaned_data['existing_medical_conditions']
			allergies = patientform.cleaned_data['allergies']
			current_medication = patientform.cleaned_data['current_medication']
			patient = Patient(age=age,sex=sex,weight=weight,location=location,existing_medical_conditions=existing_medical_conditions,allergies=allergies,current_medication=current_medication)
			# location.user = current_user
			patient.save()
		return redirect('user-profile')
	else:
		patientform = PatientForm()
	return render(request, 'user/details.html',{"message":message,"title":title,"patientform":patientform})

def doc_profile(request):
	title = "Doc's profile"
	return render(request, 'doc/profile.html',{"title":title})

def chat_home(request):
    return render(request,'chat_index.html',)

def chat(request,room_name):
	user = request.user
	room_details = Room.objects.get(name=room_name)
	return render(request,'chat/chat.html',{'room_name':room_name,'user':user,'room_details':room_details})


def check(request):
	room = request.POST['room_name']
	username = request.user
	if Room.objects.filter(name=room).exists():
		return redirect('chat',room)
	else:
		new_room = Room.objects.create(name=room)
		new_room.save()
		return redirect('chat',room)

# Create your views here.

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')


def getToken(request):
    appId = "75d978e439f2447790982442337f5626"
    appCertificate = "eb912abd811c47f7b2d0ce37b20bad92"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)