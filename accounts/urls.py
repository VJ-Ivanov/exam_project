from django.urls import path, include
from accounts.receivers import user_created
from accounts.views import SignUpView, SignOutView, SignInView, UserProfileView

urlpatterns = (
    path('', include('django.contrib.auth.urls')),
    path('profile/', UserProfileView.as_view(), name='current user profile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user profile'),
    path('signup/', SignUpView.as_view(), name='signup user'),
    path('signin/', SignInView.as_view(), name='signin user'),
    path('signout/', SignOutView.as_view(), name='signout user'),
)

