from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.datetime.now()
    return render(request, "GarfieldTheCatDay/index.html", {
        "GarfieldDay" : today.day == 19 and today.month == 6
    })