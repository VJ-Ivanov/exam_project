from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from exam_project.accounts.forms import SignUpForm, UserProfileForm
from exam_project.accounts.models import UserProfile


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('offer list view')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignInView(LoginView):
    template_name = 'accounts/signin.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('landing page')


class UserProfileView(UpdateView):
    template_name = 'accounts/user_profile.html'
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('current user profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user \
            if pk is None \
            else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.get_object().user
        context['published_companies'] = self.get_object().user.customercompany_set.all().filter(published=True)
        context['pending_companies'] = self.get_object().user.customercompany_set.all().filter(published=False)

        return context
