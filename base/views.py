from .models import Games, LastWeekGame, NextGame, Message, ImageProofs
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages




# Create your views here.
        

def home(request):  
    if request.method == 'POST':
        # username = request.POST.get("username")
        email = request.POST.get("email")
        if Message.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('/')
        message = request.POST.get("message")

        savedMesage = Message.objects.create( email=email, message=message)
        savedMesage.save()
    images = ImageProofs.objects.order_by('-id')[:2]



    next = NextGame.objects.all()
    lastWeek = LastWeekGame.objects.all()
    today = Games.objects.all()
    context = {"today": today, 'lastWeek': lastWeek, 'next': next,  'images': images}
    
    
    return render(request, 'main.html', context)

def away(request):
    allGames = Games.objects.all()
    context = {"tips": allGames}
    return render(request,'terms&conditions.html', context)

def archieve(request):
    lastWeek = LastWeekGame.objects.all()
    context = { 'lastWeek': lastWeek, 'next': next, }
    return render(request, 'archieve.html', context)

# def test(request):
#     allGames = Games.objects.all()
#     context = {"tips": allGames}
#     return render(request, 'test.html', context)