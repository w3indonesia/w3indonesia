from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User  # If views are user-specific (optional)
from django.utils.text import slugify
from ckeditor.fields import RichTextField

def validate_unicode(value):
    try:
        value.encode('utf-8')
    except UnicodeEncodeError:
        raise ValidationError('Data mengandung karakter tidak valid.')

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_unicode]) 
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=255, validators=[validate_unicode])
    content = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='news_articles', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    author = models.CharField(max_length=255, validators=[validate_unicode])
    views = models.PositiveIntegerField(default=0)  # Still keep this for total views

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class NewsArticleView(models.Model):
    news_article = models.ForeignKey(
        NewsArticle, 
        related_name='article_views',  # Custom related_name to avoid conflict
        on_delete=models.CASCADE
    )
    viewed_at = models.DateTimeField(default=now)  # Timestamp for when the view occurred
    viewer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Optional: track who viewed

    def __str__(self):
        return f"View for {self.news_article.title} at {self.viewed_at}"


