from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserRegistrationForm
from django.contrib.auth import login
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import LoginForm  # Assuming you have a custom login form
from django.contrib.auth import authenticate, login

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('authentication:dashboard')

    def form_valid(self, form):
        # Your custom authentication logic here
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print ("")
        # Custom authentication logic based on your CustomUser model
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            # Log in the user
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            # Invalid credentials
            return self.form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = 'authentication:login'  # Redirect to the login page after logout

@csrf_protect
def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('authentication:login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, "authentication/register.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def home(request):
    return render(request, 'authentication/home.html')
