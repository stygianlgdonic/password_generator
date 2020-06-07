from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, "home.html")


def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")

    length = int(request.GET.get("length", 8))

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()_"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    my_password = ""
    for x in range(length):
        my_password += random.choice(characters)

    return render(request, "password.html", {"password": my_password})
