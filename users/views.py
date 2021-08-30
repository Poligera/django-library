from users.forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form_data = UserRegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            username = form_data.cleaned_data.get('username')
            messages.success(request, f"Welcome, {username}!")
            return redirect('books-index') # will change to books-show later
    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)