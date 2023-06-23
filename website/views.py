from django.shortcuts import render

# Create your views here.

context_dictionary = {}

def home(request):
    return render(request, 'home.html', context_dictionary)

def contact(request):
    return render(request, 'contact.html', context_dictionary)