from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Salom dunyo")

def users(request):
    users_data = {
        "users": ["User1", "User2", "User3", "User4", "User5"]
    }
    return JsonResponse(users_data)

def ads(request):
    context = {
        'ad_headline': 'Amazing Offer!',
        'ad_body': 'Get 50% off your next purchase!',
        'ad_image_url': 'path/to/your/image.jpg' 
    }
    return render(request, 'advertisement/ads.html', context)