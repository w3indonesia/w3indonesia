from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError

def validate_unicode(value):
    try:
        value.encode('utf-8')
    except UnicodeEncodeError:
        raise ValidationError('Data mengandung karakter tidak valid.')

class Category(models.Model):
    name = models.CharField(max_length=255, validators=[validate_unicode])
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100, validators=[validate_unicode]) 
    order = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.__original_name:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.name

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, validators=[validate_unicode])
    slug = models.SlugField(unique=False, max_length=100, validators=[validate_unicode])
    order = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.__original_name:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Subcategory.objects.filter(slug=slug, category=self.category).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.name

    class Meta:
        unique_together = ('slug', 'category')
        ordering = ['order']


    def __str__(self):
        return self.name




class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    ]

    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[validate_unicode])
    slug = models.SlugField(max_length=100, validators=[validate_unicode])
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.__original_title:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Article.objects.filter(slug=slug, subcategory=self.subcategory).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_title = self.title

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            UniqueConstraint(fields=['subcategory', 'slug'], name='unique_slug_in_subcategory')
        ]
        ordering = ['order']

