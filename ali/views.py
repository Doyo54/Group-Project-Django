from django.shortcuts import render
from doyo.models import Profile
from doyo.models import Patient

# Create your views here.

def profile(request, id):
    profile= Profile.objects.get_or_create(user=request.user)

    return render(request, 'user_profile.html')
