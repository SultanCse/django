from django.shortcuts import render
from .models import Products_list

# Create your views here.
def home(request):
    x = Products_list.objects.all()
    return render(request,'home.html', {'x': x})


