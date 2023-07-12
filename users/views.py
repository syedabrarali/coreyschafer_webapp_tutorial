from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
     if request.method == "POST":
          u_form = UserUpdateForm(request.POST, instance=request.user)
          p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
     # above request.FILES is to get the image file which the user will upload and request.POST 
     # is whatever the user submtis, the instance arguments shows us the current info saved in those fields by 
     # invoking the models
          if u_form.is_valid() and p_form.is_valid():
               u_form.save()
               p_form.save()
               messages.success(request, 'Your account has been updated')
               return redirect('profile')
     else:
          u_form = UserUpdateForm(request.POST, instance=request.user)
          p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)      
     context = {
          'u_form': u_form,
          'p_form': p_form
     }
     return render(request, 'users/profile.html', context)