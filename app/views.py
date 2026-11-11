from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "app/home.html")


def foods(request):
    foods = ["Shrimp", "Steak", "Spaghetti", "Cheese"]
    context = {
        "foods": foods,
    }
    return render(request, "app/foods.html", context)
