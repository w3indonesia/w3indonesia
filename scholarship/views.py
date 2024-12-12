from django.shortcuts import render

def under_construction(request):
    return render(request, 'scholarship/under_construction.html')
