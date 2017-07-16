from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import VJLoginForm, VJSignUpForm

def vj_login(request):
    if request.method == 'POST':
        form = VJLoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']
            user = authenticate(request, userid =userid, password = password)
        else:
            return render(request, 'user/login.html', {'form': form})
        # user의 값이 is_active도 체크
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'main/main.html', {})
    else:
        return render(request, 'user/login.html', {'form': VJLoginForm()})

def vj_signup(request):
    if request.method == 'POST':
        form = VJSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
        else:
            return render(request, 'user/signup.html', {'form': form})
    else:
        return render(request, 'user/signup.html', {'form': VJSignUpForm()})

def vj_logout(request):
    logout(request)
    return redirect('user:login')
