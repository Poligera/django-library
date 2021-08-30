from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form_data = UserRegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()

            # LOGIN straightaway:
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password1')
            new_user = authenticate(request, username=username, password=password) # built-in. Verifies credentials
            login(request, new_user)

            messages.success(request, f"Welcome, {username}!") # not working!
            return redirect('books-index') # will change to books-show later
        else:
            messages.error(request, form_data.errors)
    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)


# CAREFUL - use different name from import "login"
def login_request(request):
    if request.method == "POST":
        form_data = AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome, {username}!")
                return redirect('books-index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        login_form = AuthenticationForm()
        context = {'login_form': login_form}
        return render(request, 'users/login.html', context)


# CAREFUL - use different name from import "logout"
def logout_request(request):
    return render(request, 'users/logout.html')