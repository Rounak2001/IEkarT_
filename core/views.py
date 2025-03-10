from django.shortcuts import render, redirect
from django.contrib import messages
from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def faq_view(request):
    return render(request, 'core/faq.html')

def about(request):
    return render(request, 'core/about.html')

def logout(request):
    return render(request, 'core/logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

             # Set a success message
            messages.success(request, 'Registered successfully.')

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })