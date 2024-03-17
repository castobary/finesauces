from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .forms import LoginForm, UserRegistrationForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cf = form.cleaned_data
            user_record = None
            try:
                user_record = User.objects.get(email=cf['email'])
            except User.DoesNotExist:
                pass

            if user_record:
                user = authenticate(
                    request,
                    username=user_record,
                    password=cf['password']
                )

                if user is not None:
                    login(request, user)
                    return redirect('listings:product_list')
            
            messages.error(request, 'Incorrect email/password')
        
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

class UserLogoutView(LogoutView):
    """custom logout view"""

    def get_next_page(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "You successfully log out!",
            extra_tags="alert-success",
        )
        return super().get_next_page()
    
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cf = user_form.cleaned_data

            email = cf['email']
            password = cf['password']
            password2 = cf['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                    messages.error(request,
                        'User with given email already exists')
                    return render(
                        request,
                        'accounts/register.html',
                        {'user_form': user_form}
                    )
        else:
            messages.error(request, 'Passwords don\'t match')
            return render(
                        request,
                        'accounts/register.html',
                        {'user_form': user_form}
                    )
        # Create a new user object
        new_user = User.objects.create_user(
                first_name=cf['first_name'],
                last_name=cf['last_name'],
                username=email,
                email=email,
                password=password
            )

        return render(
                request,
                'accounts/register_done.html',
                {'new_user': new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        'accounts/register.html',
        {'user_form': user_form}
    )


