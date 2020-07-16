from django.shortcuts import render
from .models import Wish


def home(request):
    wish=Wish.objects.all()
    return render(request,'wishes/home.html',{'wish':wish})
