from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from .models import NewsArticle, Category as NewsCategory
from tutorial.models import Category as TutorialCategory

def get_popular_articles():
    return NewsArticle.objects.filter(is_published=True).order_by('-views')[:5]

def news_list(request):
    top_categories = NewsCategory.objects.all() 
    popular_articles = get_popular_articles() 
    news_articles = NewsArticle.objects.filter(is_published=True).order_by('-published_date')
    tutorial_categories = TutorialCategory.objects.all() 

    newest_articles = news_articles[:3]
    featured_news = NewsArticle.objects.filter(is_featured=True, is_published=True).order_by('-published_date')[:3]

    section_mari_belajar = {"section": "mari_belajar"}
    
    paginator = Paginator(news_articles, 10)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    return render(request, 'news/news_list.html', {
        'news_articles': news_articles,
        'popular_articles': popular_articles,  
        'top_categories': top_categories,
        'page_obj': page_obj,
        'newest_articles': newest_articles,
        'featured_news': featured_news,
        'tutorial_categories': tutorial_categories,
        'section_mari_belajar': section_mari_belajar,
    })

def news_detail(request, category_slug, news_slug):
    news_article = get_object_or_404(NewsArticle, slug=news_slug, category__slug=category_slug)
    news_urls = NewsArticle.objects.all().order_by('-published_date')
    popular_articles = get_popular_articles()
    tutorial_categories = TutorialCategory.objects.all() 

    return render(request, 'news/news_detail.html', {
        'news_urls': news_urls,
        'news_article': news_article,
        'popular_articles': popular_articles,
        'tutorial_categories': tutorial_categories,
    })

def news_by_category(request, category_slug):
    category = get_object_or_404(NewsCategory, slug=category_slug)
    news_articles = NewsArticle.objects.filter(category=category, is_published=True).order_by('-published_date')

    paginator = Paginator(news_articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_categories = NewsCategory.objects.all()

    context = {
        'category': category,
        'all_categories': all_categories,
        'news_articles': news_articles,
        'page_obj': page_obj,
        'popular_articles': get_popular_articles(),
    }
    return render(request, 'news/news_by_category.html', context)

def news_page(request, page_number=1):
    news_categories = NewsCategory.objects.all() 
    news_articles = NewsArticle.objects.filter(is_published=True).order_by('-published_date')
    tutorial_categories = TutorialCategory.objects.all() 
    section_mari_belajar = {"section": "mari_belajar"}
    
    paginator = Paginator(news_articles, 10)
    
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    
    articles_list = list(page_obj.object_list)
    
    return render(request, 'news/news_page.html', {
        'page_obj': page_obj,
        'articles_list': articles_list, 
        'tutorial_categories': tutorial_categories,
        'news_categories': news_categories,
    })


