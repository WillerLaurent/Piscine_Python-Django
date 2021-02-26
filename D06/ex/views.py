from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import random
from .forms import Login, Connect, TipForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from ex.models import Tip
from django.http import HttpResponse


def home(request):
    form = TipForm()
    tips = Tip.objects.all().order_by('date')
    if request.method == "POST":
        tipform = TipForm(request.POST)
        if tipform.is_valid():
            data = tipform.cleaned_data
            tip = Tip(contenu=data['contenu'], auteur=request.user.username)
            tip.save()
            print("Nouveau tip créé", tip)
    if request.COOKIES.get('mycookie'):
        user1 = request.COOKIES['mycookie']
        response = render(request, 'accueil.html', {'user1': user1, 'form': form, 'tips': tips})
    else:
        # s'il n'y a pas de cookie ou le précédent est périmé
        user1 = random.choice(settings.USER_NAMES)
        response = render(request, 'accueil.html', {'user1': user1, 'form': form, 'tips': tips})
        response.set_cookie('mycookie', user1, max_age=settings.SESSION_COOKIE_DURATION)

    return response


def inscription(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(data['username'], None, data['password'])
            u.save()
            auth.login(request, u)
            #  print('Utilisateur créé et logué :', us1)
            return redirect('/')
    else:  # méthode GET
        form = Login()

    return render(request, 'login.html', {'form': form})


def connexion(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = Connect(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = auth.authenticate(username=data['username'], password=data['password'])
            if u and u.is_active:
                auth.login(request, u)
                return redirect('/')
            else:
                form.errors['username'] = ["Mot de passe ou nom d'utilisateur inconnu"]
    else:
        form = Connect()

    return render(request, 'connexion.html', {'form': form})


def deconnexion(request):
    auth.logout(request)
    return redirect('/')
