from django.shortcuts import render

# Create your views here.


def home(request):
    foods = ["Shrimp", "Steak", "Spaghetti", "Cheese"]
    context = {
        "foods": foods,
    }
    return render(request, "app/home.html", context)
