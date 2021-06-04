import random

from django.shortcuts import render

# Create your views here.
names = ["ama", "rose", "felicia", "akua", "amanda", "sitegal"]


def home(request):
    return render(request, "generator/home.html")


def about(request):
    return render(request, "generator/about.html")


def password(request):
    passwordgen = ""
    characters = list("")
    uppercase = request.GET.get("uppercase")
    lowercase = request.GET.get("lowercase")
    if lowercase:
        characters.extend(list("abcdefghijklmnopqrstuvwxyz"))
    if uppercase:
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    special = request.GET.get("special")
    if special:
        characters.extend(list("!@#$%^&*()_+?><:;"))

    numbers = request.GET.get("numbers")
    if numbers:
        characters.extend(list("1234567890"))

    length = int(request.GET.get("length", 12))
    for x in range(length):
        passwordgen += random.choice(characters)

    if passwordgen:
        return render(request, "generator/password.html", {"password": passwordgen})
    else:
        return render(request, "generator/home.html")
