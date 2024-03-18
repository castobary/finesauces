from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html'), name='login'),
     path('login/', views.user_login, name='login'),
     path('register/', views.register, name='register'),
     path('profile/',views.profile, name='profile'),
     path('logout/', views.UserLogoutView.as_view(), name='logout'),
     path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')),name='password_change'),
     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
     path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),name='password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     path('password_reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),name='password_reset_confirm'),
     path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
