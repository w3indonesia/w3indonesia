from django.shortcuts import render, get_object_or_404
from .models import Job
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from django.core.paginator import Paginator

def job_list(request):
    job = Job.objects.all()  # Get all jobs
    paginator = Paginator(job, 10)  # Show 10 jobs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs/job_list.html', {'page_obj': page_obj})


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)  # Get job by slug
    
    similar_jobs = Job.objects.annotate(
        similarity=TrigramSimilarity('title', job.title)
    ).filter(
        ~Q(slug=job.slug),  # Exclude the current job
        similarity__gt=0.3  # Similarity threshold
    ).order_by('-similarity')

    if similar_jobs.count() < 10:
        fallback_jobs = Job.objects.filter(
            ~Q(slug=job.slug)
        ).order_by('-posted_at')[:10 - similar_jobs.count()]
        similar_jobs = list(similar_jobs) + list(fallback_jobs)

    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'similar_jobs': similar_jobs,
    })


def job_search(request):
    query = request.GET.get('query', '')
    
    # Get all jobs
    jobs = Job.objects.all()

    # If there’s a query, filter jobs based on the search term
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(industry__icontains=query) |
            Q(job_type__icontains=query) |
            Q(salary__icontains=query) |
            Q(work_schedule__icontains=query)
        )
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 5 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs/job_search.html', {
        'page_obj': page_obj,
        'query': query
    })
