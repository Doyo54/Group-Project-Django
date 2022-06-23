from django.shortcuts import render
from .models import Profile

# Create your views here.

def profile(request, id):
    profile= Profile.objects.get_or_create(user=request.user)
    user_prof = Profile.objects.get(id=id)
    return render(request, 'user_profile.html')
