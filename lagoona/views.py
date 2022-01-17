from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *




class AllHotelsList(ListView):
    model = Hotel
    queryset = Hotel.objects.all()
    template_name = 'lagoona_all_hotels.html'
    context_object_name = 'hotels'

def test(request, slug):
    first_hotel = Hotel.objects.get(slug=slug)
    return render(request, 'test.html', {'hotel': first_hotel})

def test_tour(request):
    return render(request, 'test.html', {})

def index(request):
    first_hotel = Hotel.objects.all()[:9]
    spec_offer = Tours.objects.all()[:2]
    return render(request, 'lagoona.html', {'hotels': first_hotel, 'spec_offer': spec_offer})

class RegisterUser(CreateView):
    template_name = 'lagoona_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class AuthenticationUser(LoginView):
    form_class = LoginForm
    template_name = 'lagoona_login.html'

def logout_user(request):
    logout(request)
    return redirect('login')
