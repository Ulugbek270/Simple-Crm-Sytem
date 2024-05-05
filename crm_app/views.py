from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *


# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST["username"]  # Cuz home.html we gave it
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Some error occured")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:

        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:

        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records deleted successfully")
        return redirect('home')

    else:
        messages.warning(request, "You must be logged in")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Records added successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.warning(request, "You must be logged in")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
