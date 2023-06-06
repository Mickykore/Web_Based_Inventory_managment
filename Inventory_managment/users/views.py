from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f"{username}")
            messages.success(request, f'Account created successfully pleace login')
            return redirect('login')
    else:
        form = UserRegisterForm()
        messages.error(request, f'error')
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        update_user_form = UserUpdateForm(request.POST, instance=request.user)
        update_profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        update_user_form = UserUpdateForm(instance=request.user)
        update_profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form,
    }

    return render(request, 'users/profile.html', context)