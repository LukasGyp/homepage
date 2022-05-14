from http.client import HTTPResponse
from django.shortcuts import render
from .models import Profile

# Create your views here.
def top(request):
  return render(request, 'top.html')

def profile(request):
  context = {
    'prof': Profile.objects.first()
  }
  return render(request, 'profile.html', context)