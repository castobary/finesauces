from django.urls import path
from . import views
from django.views.decorators.http import require_http_methods
#from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html'), name='login'),
     path('login/', views.user_login, name='login'),
   #  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
