from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
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
