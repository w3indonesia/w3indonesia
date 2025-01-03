from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Scholarship
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

def scholarship_list(request):
    scholarships = Scholarship.objects.all()

    # Paginasi: Tampilkan 10 beasiswa per halaman
    paginator = Paginator(scholarships, 10)
    page_number = request.GET.get('page', 1)  # Halaman default 1
    page_obj = paginator.get_page(page_number)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Render ulang bagian HTML untuk daftar beasiswa
        html = render_to_string("scholarships/scholarship_list_ajax.html", {"page_obj": page_obj})
        return JsonResponse({"html": html, "has_next": page_obj.has_next()})

    return render(request, "scholarships/scholarship_list.html", {"page_obj": page_obj})



def scholarship_detail(request, slug):
    scholarship = get_object_or_404(Scholarship, slug=slug)
    return render(request, 'scholarships/scholarship_detail.html', {'scholarship': scholarship})



def scholarship_search(request):
    query = request.GET.get('query', '')
    scholarships = Scholarship.objects.all()

    # Jika ada query, filter berdasarkan kata kunci di berbagai atribut
    if query:
        scholarships = scholarships.filter(
            Q(description__icontains=query) |
            Q(provider__icontains=query) |
            Q(location__icontains=query)
        )

    # Paginasi: Tampilkan 5 hasil per halaman
    paginator = Paginator(scholarships, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'scholarships/scholarship_search.html', {
        'page_obj': page_obj,
        'query': query
    })
