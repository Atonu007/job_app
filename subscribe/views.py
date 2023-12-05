from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Subscribe
from .forms import SubscribeForms

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForms
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForms(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
       
    context = {'form': subscribe_form,'email_error_empty': email_error_empty, }
    return render(request,'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)