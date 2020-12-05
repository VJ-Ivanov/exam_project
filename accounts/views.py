from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm
from accounts.models import UserProfile


def user_profile(request, pk):
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