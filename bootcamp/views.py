from django.shortcuts import render

def under_construction(request):
    return render(request, 'bootcamp/under_construction.html')
