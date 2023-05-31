from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f"{username}")
            messages.success(request, f'Account created successfully pleace login')
            return redirect('login')
    else:
        form = UserCreationForm()
        messages.error(request, f'error')
    return render(request, 'users/register.html', {'form': form})
