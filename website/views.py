from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddForm
from .models import Record
# Create your views here.


def home(request):
    records = Record.objects.all()
    # check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged in.")
            return redirect("home")
        else:
            messages.error(request, "There was an error!")
            return redirect("home")
    else:
        return render(request, "home.html", {'records': records})


def login_user(request):
    pass


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You Have Successfully Registered! Welcome!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out..")
    return redirect("home")


def cust_record(req, pk):
    if req.user.is_authenticated:
        # look up record
        cust_record = Record.objects.get(id=pk)
        return render(req, 'record.html', {'cust_record': cust_record})
    else:
        messages.warning(req, "Log in first")
        return redirect('home')


def delete_record(req, pk):
    if req.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(req, "Record deleted")
        return redirect('home')
    else:
        messages.warning(req, "Must be Logged in")
        return redirect('home')


def add_record(req):
    form = AddForm(req.POST or None)
    if req.user.is_authenticated:
        if req.method == "POST":
            form.save()
            messages.success(req, "Record Added")
            return redirect('home')
        return render(req, 'add.html', {'form': form})
    else:
        messages.warning(req, "Must be Logged in")
        return redirect('home')


def update_record(req, pk):
    if req.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddForm(req.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(req, "Record Updated")
            return redirect('home')
        return render(req, "update.html", {'form': form})
    else:
        messages.error(req,"You have to log in to update a record.")
        return redirect('home')
