from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return render(request, 'index.html')

def searchresults(request):
    response = "You're looking at the search results."
    return HttpResponse(response)

def profile(request):
    return HttpResponse("You're looking at the profile.")
