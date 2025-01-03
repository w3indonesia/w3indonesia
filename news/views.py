from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import now, timedelta
from .models import NewsArticle, NewsArticleView, Category
from tutorial.models import Category as TutorialCategory
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Count

def get_popular_articles():
    return NewsArticle.objects.filter(is_published=True).order_by('-views')[:10]

def get_trending_articles():
    one_month_ago = now() - timedelta(days=30)
    return NewsArticle.objects.filter(
        is_published=True,
        published_date__gte=one_month_ago
    ).order_by('-views')[:3]

def load_more_news(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check if it's an AJAX request
        page = int(request.GET.get('page', 1))  # Get the page number from the query parameter
        news_articles = NewsArticle.objects.filter(is_published=True).order_by('-published_date')

        # Paginator: Load only 1 article per page
        paginator = Paginator(news_articles, 10)  # We want to load 1 article at a time
        page_obj = paginator.get_page(page)

        # Render HTML for the new articles
        html = render_to_string('news/news_list_ajax.html', {'page_obj': page_obj}, request=request)

        # Return JSON with the rendered HTML and a flag indicating if there are more pages
        return JsonResponse({"html": html, "has_next": page_obj.has_next()})

    return JsonResponse({"error": "Invalid request"}, status=400)




def news_list(request):
    # Fetch all published news articles
    news_articles = NewsArticle.objects.filter(is_published=True).select_related('category').order_by('-published_date')

    # Popular articles based on view counts
    popular_articles = (
        NewsArticle.objects.filter(is_published=True)
        .annotate(view_count=Count('article_views'))
        .order_by('-view_count')[:5]
    )

    # Trending articles (top 2 by views)
    trending_articles = (
        NewsArticle.objects.filter(is_published=True)
        .annotate(view_count=Count('article_views'))
        .order_by('-view_count')[:2]
    )

    # Get all categories with article counts
    news_categories = Category.objects.annotate(article_count=Count('news_articles')).filter(article_count__gt=0)

    # Latest three featured articles
    featured_articles = news_articles.filter(is_featured=True)[:3]

    # Featured news and newest articles
    featured_news = news_articles.filter(is_featured=True)[:3]
    newest_articles = news_articles[:3]

    # Validate newest articles data
    for article in newest_articles:
        article.has_valid_data = bool(article.category and article.slug)

    # Pagination
    paginator = Paginator(news_articles, 10)  # Adjust the number of articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Re-render only the article list for AJAX requests
        html = render_to_string("news/news_list_ajax.html", {"page_obj": page_obj}, request=request)
        return JsonResponse({"html": html, "has_next": page_obj.has_next()})

    # Render the full page
    return render(request, 'news/news_list.html', {
        'news_articles': news_articles,
        'popular_articles': popular_articles,
        'trending_articles': trending_articles,
        'featured_articles': featured_articles,
        'featured_news': featured_news,
        'newest_articles': newest_articles,
        'tutorial_categories': TutorialCategory.objects.all(),
        'page_obj': page_obj,
        'news_categories': news_categories,
        'data_not_available': any(not article.has_valid_data for article in newest_articles),
    })


def news_detail(request, category_slug, news_slug):
    # Fetch article and related data
    news_article = get_object_or_404(NewsArticle, slug=news_slug, category__slug=category_slug)
    tutorial_categories = TutorialCategory.objects.all()
    popular_articles = get_popular_articles()

    # Log the view
    NewsArticleView.objects.create(
        news_article=news_article,
        viewed_at=now(),
        viewer=request.user if request.user.is_authenticated else None
    )

    # Update total views
    news_article.views += 1
    news_article.save(update_fields=['views'])

    return render(request, 'news/news_detail.html', {
        'news_article': news_article,
        'popular_articles': popular_articles,
        'tutorial_categories': tutorial_categories,
    })

def category_articles(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    news_articles = NewsArticle.objects.filter(category=category, is_published=True).order_by('-published_date')

    paginator = Paginator(news_articles, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.get_page(1)

    all_categories = Category.objects.all()

    return render(request, 'news/news_by_category.html', {
        'category': category,
        'news_articles': news_articles,
        'page_obj': page_obj,
        'all_categories': all_categories,
        'popular_articles': get_popular_articles(),
    })


def news_page(request, page_number=1):
    news_categories = Category.objects.all()
    news_articles = NewsArticle.objects.filter(is_published=True).order_by('-published_date')
    tutorial_categories = TutorialCategory.objects.all()

    paginator = Paginator(news_articles, 10)
    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.get_page(1)

    return render(request, 'news/news_page.html', {
        'page_obj': page_obj,
        'tutorial_categories': tutorial_categories,
        'news_categories': news_categories,
    })
