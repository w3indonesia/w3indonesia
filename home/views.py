from django.shortcuts import render
from tutorial.models import Category  # Pastikan model Category sudah benar diimpor

def home(request):
    categories = Category.objects.all()  # Ambil semua kategori
    context = {
        'categories': categories
    }
    return render(request, 'home/home.html', context)
