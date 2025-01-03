from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.html import strip_tags
from django.db.models import Count
from .models import Category, Project, Stage, Article

def focuus_home(request):
    projects = Project.objects.all().order_by('order')
    categories = Category.objects.all().order_by('order')
    stages = Stage.objects.all().order_by('order')
    return render(request, 'focuus/focuus_home.html', {
        'projects': projects,
        'categories': categories,
        'stages': stages,
        })

def focuus_page(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    category.views += 1
    category.save()
    
    stages = category.stages.prefetch_related('articles')
    top_categories = Category.objects.order_by('-views')[:10]
    categories = Category.objects.all()

    context = {
        'category': category,
        'categories': categories,
        'stages': stages,
        'top_categories': top_categories,
    }
    return render(request, 'tutorial/tutorial_page.html', context)

def focuus_list(request, category_slug, stage_slug):
    category = get_object_or_404(Category, slug=category_slug)
    stage = get_object_or_404(Stage, slug=stage_slug, category=category)
    articles = Article.objects.filter(stage=stage)
    
    context = {
        'category': category,
        'stage': stage,
        'articles': articles,
    }
    return render(request, 'tutorial/article_list.html', context)

def focuus_detail(request, category_slug, stage_slug, article_slug):
    article = get_object_or_404(
        Article,
        slug=article_slug,
        stage__slug=stage_slug,
        stage__category__slug=category_slug
    )

    if article.status != 'publish':
        raise Http404("Artikel tidak ditemukan atau masih dalam status draft.")

    category = article.stage.category
    stage = article.stage
    
    stages = Stage.objects.filter(category=category).order_by('order')
    articles_in_stage = Article.objects.filter(stage=stage).order_by('order')

    previous_article = (
        articles_in_stage
        .filter(order__lt=article.order)
        .order_by('-order') 
        .first()
    )

    if not previous_article:
        previous_stage = stages.filter(order__lt=stage.order).last()
        if previous_stage:
            previous_article = previous_stage.articles.order_by('-order').first()

    next_article = (
        articles_in_stage
        .filter(order__gt=article.order)
        .order_by('order') 
        .first()
    )

    if not next_article:
        next_stage = stages.filter(order__gt=stage.order).first()
        if next_stage:
            next_article = next_stage.articles.order_by('order').first()

    description = strip_tags(article.content)[:150] if article.content else "Baca tutorial di w3indonesia.com!"
    image_url = 'https://w3indonesia.com/static/img/default-thumbnail.jpg'
    if hasattr(article, 'image') and article.image:
        image_url = article.image.url  

    current_url = request.build_absolute_uri()

    return render(request, 'tutorial/article_detail.html', {
        'article': article,
        'previous_article': previous_article,
        'next_article': next_article,
        'stage': stage,
        'stages': stages,
        'category': category,
        'request': request,
        'description': description,
        'image_url': image_url,
        'current_url': current_url,
    })

# Custom error views
def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})

def error_401(request, exception=None):
    return render(request, 'errors/401.html', status=401)

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def error_405(request, exception=None):
    return render(request, 'errors/405.html', status=405)

def error_429(request, exception=None):
    return render(request, 'errors/429.html', status=429)

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def error_502(request, exception=None):
    return render(request, 'errors/502.html', status=502)

def error_503(request, exception=None):
    return render(request, 'errors/503.html', status=503)
