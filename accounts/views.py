from typing import Any, Dict, Optional
from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from django.views.generic import TemplateView,RedirectView
from .forms import UserRegistrationForm, UserAddressForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView

# Create your views here.
User = get_user_model()

class UserRegistrationView(TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name=''#fill korte hobe
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(
                reverse_lazy()#fill korte hobe
            )
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(self.request.POST)
        address_form = UserAddressForm(self.request.POST)
        
        if registration_form.is_valid() and address_form.is_valid():
            user = registration_form.save()
            address = address_form.save()
            address.user = user
            address.save()
            
            login(self.request, user)
            messages.success(
                self.request,
                (
                    f'Thank You For Creating A Bank Account. '
                    f'Your Account Number is {user.account.account_no}.'
                )
            )
            return HttpResponseRedirect(
                reverse_lazy()#fill korte hobe
            )
        return self.render_to_response(
            self.get_context_data(
                registration_form=registration_form,
                address_form=address_form
            )
        )
            
    def get_context_data(self, **kwargs):
        if 'registration_form' not in kwargs:
            kwargs['registration_form'] = UserRegistrationForm()
            
        if 'address_form' not in kwargs:
            kwargs['address_form'] = UserAddressForm()
        
        return super().get_context_data(**kwargs)  

class UserLoginView(LoginView):
    template_name=''#fill korte hobe
    redirect_authenticated_user = False
    

class LogoutView(RedirectView):
    pattern_name = ''#fill korte hobe
    
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
    
    
    
