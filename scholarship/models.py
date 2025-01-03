from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Scholarship(models.Model):
    provider = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = RichTextField()
    eligibility = RichTextField()
    grade_s1_status = models.BooleanField(default=False)  # Status for S1
    grade_s2_status = models.BooleanField(default=False)  # Status for S2
    grade_s3_status = models.BooleanField(default=False)  # Status for S3
    applicable_program = RichTextField(default="N/A")
    requirement = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=255, default="N/A")
    age = models.PositiveIntegerField(default=0)
    ielts = models.PositiveIntegerField(default=0, null=True, blank=True)
    toefl = models.PositiveIntegerField(default=0, null=True, blank=True)
    application_deadline = models.DateField()
    scholarship_amount = models.CharField(max_length=255, default="N/A")
    scholarship_coverage = RichTextField(null=True, blank=True)
    contact_email = models.EmailField()
    website = models.URLField()
    views = models.PositiveIntegerField(default=0)  # Views counter
    posted_at = models.DateTimeField(auto_now_add=True)  # Time of posting

    class Meta:
        ordering = ['-posted_at']  # Order by newest first

    def save(self, *args, **kwargs):
        # Generate slug automatically from the provider if not already set
        if not self.slug:
            base_slug = slugify(self.provider)
            unique_slug = base_slug
            counter = 1
            while Scholarship.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.provider
