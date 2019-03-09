from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.


def register(request):
    post_ = request.get_full_path().split('/')[1]
    if post_ == 'register':
        post_ = 'anymore no ...'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  #created user adding to dbase
            user_name = form.cleaned_data.get('username')
            message_text = 'Account is created for '+user_name
            messages.success(request, message_text)
            new_user = authenticate(request, username=user_name, password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('screen-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',
                  {'form': form, 'title': 'register', 'post': post_})


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': 'profile'})