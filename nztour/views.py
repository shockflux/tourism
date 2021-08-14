from django.shortcuts import render, redirect
from .models import destination
from .forms import RegisterForm

# Create your views here.
def index(request):
    dests = destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def tours(request, name):
    obj = destination.objects.get(name=name)
    context = {
        "objects":obj
    }
    return render(request, "tours.html", context)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})
