from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'profile_user': user
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
         pass


def signup_user(request):
    if request.method == "GET":
        context = {
            'form': SignUpForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            profile = UserProfile(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('landing page')
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)