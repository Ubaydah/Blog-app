from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/complete.html'), name='password_reset_complete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
