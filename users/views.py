from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, 'Your account has been created, you can now Login!')
               return redirect('login') #returns to the login view once the user has been registered
     else:     
        form = UserRegisterForm()
     context = {
          'form': form
     }
     return render(request, 'users/register.html', context)

@login_required #this makes sure that a user is logged in to view the profile view
def profile(request):
     return render(request, 'users/profile.html')