from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError

# Validator for Unicode
def validate_unicode(value):
    try:
        value.encode('utf-8')
    except UnicodeEncodeError:
        raise ValidationError('Data contains invalid characters.')

# 1. Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, validators=[validate_unicode])
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100, validators=[validate_unicode])
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != getattr(self, '__original_name', None):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.name

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

# 2. Project Model
class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, validators=[validate_unicode])
    description = models.TextField(blank=True)  # General project description
    requirements = RichTextField(blank=True, null=True)  # Requirements to complete the project
    final_product_description = models.TextField(blank=True, null=True)  # Description of the final product
    slug = models.SlugField(unique=True, max_length=100, validators=[validate_unicode])
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != getattr(self, '__original_name', None):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.name

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


# 3. Stage Model
class Stage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stages')
    order = models.IntegerField(default=0)  # Determines the stage order
    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        # Automatically generate the stage name as 'Stage <order>'
        self.name = f"Stage {self.order}"
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 1

        # Ensure unique slugs
        while Stage.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Stage {self.order} ({self.project.name})"


# 4. Article Model
class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    ]

    stage = models.ForeignKey(Stage, related_name='articles', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='articles', on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE, default=None)
    
    title = models.CharField(max_length=255, validators=[validate_unicode])
    slug = models.SlugField(max_length=100, validators=[validate_unicode])
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug or self.title != getattr(self, '__original_title', None):
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Article.objects.filter(slug=slug, stage=self.stage).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_title = self.title

    class Meta:
        unique_together = ('slug', 'stage')
        ordering = ['order']

    def __str__(self):
        return self.title

