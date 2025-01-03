from django.shortcuts import render
from tutorial.models import Category 

def home(request):
    categories = Category.objects.all() 
    context = {
        'categories': categories
    }
    return render(request, 'home/home.html', context)
