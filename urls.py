from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as myapp_views


urlpatterns = [
    path('', myapp_views.home, name="home"),
    path('register', myapp_views.regiter, name='register'),
    path('login', myapp_views.login_view, name='login'),
    path('logout', myapp_views.logout_view, name='logout'),
    path('profile', myapp_views.profile, name='profile'),

    path('password-reset', myapp_views.CustomPasswordResetView, name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]