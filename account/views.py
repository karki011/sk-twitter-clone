from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Your accout has been created! Now you can login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'twitterclone/register.html', {'form': form})

