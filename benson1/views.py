from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	message = 'Hello, Africa'
	title = 'Home'
	return render(request, 'index.html',{"message":message,"title":title})


def doc(request):
	message = 'Just testing things for now'
	title = "Doc's details"
	return render(request, 'doc/credentials.html',{"message":message,"title":title})

def doc_profile(request):
	title = "Doc's profile"
	return render(request, 'doc/profile.html',{"title":title})
