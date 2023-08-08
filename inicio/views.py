from django.contrib.auth.views import LoginView
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CustomLoginForm, CustomRegistrationForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

class CustomLogoutView(LoginView):
    template_name = 'logout.html'
    success_url = reverse_lazy('login')


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al usuario a la página de inicio de sesión
            return HttpResponseRedirect(reverse('login'))
    else:
        form = CustomRegistrationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'index.html')

# Create your views here.
