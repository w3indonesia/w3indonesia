from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

# Validator untuk memastikan hanya karakter Unicode yang valid
def validate_unicode(value):
    try:
        value.encode('utf-8')
    except UnicodeEncodeError:
        raise ValidationError('Data mengandung karakter tidak valid.')

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_unicode])  # Menambahkan validator di sini
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=255, validators=[validate_unicode])  # Menambahkan validator di sini
    content = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='news_articles', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    author = models.CharField(max_length=255, validators=[validate_unicode])  # Menambahkan validator di sini
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
