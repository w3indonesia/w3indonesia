from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Job(models.Model):
    title = models.CharField(max_length=255)  # Posisi Pekerjaan
    slug = models.SlugField(max_length=255, unique=True)  # Slug for URL
    location = models.CharField(max_length=255)  # Lokasi Pekerjaan
    company = models.CharField(max_length=255)  # Nama Perusahaan
    industry = models.CharField(max_length=255, blank=True, null=True)  # Jenis Industri
    qualifications = RichTextField(blank=True, null=True)  # Kualifikasi
    description = RichTextField()  # Deskripsi Pekerjaan
    benefits = RichTextField(blank=True, null=True)  # Benefit
    job_level = models.CharField(max_length=255, blank=True, null=True)  # Level Pekerjaan
    job_type = models.CharField(max_length=255, blank=True, null=True)  # Tipe Pekerjaan
    salary = models.CharField(max_length=255, blank=True, null=True)  # Gaji
    work_schedule = models.CharField(max_length=255, blank=True, null=True)  # Jadwal Kerja
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)  # Logo Perusahaan
    posted_at = models.DateTimeField(default=timezone.now)  # Tanggal Posting
    expiration_date = models.DateTimeField(blank=True, null=True)  # Tanggal Kadaluarsa
    apply_link = models.URLField(blank=True, null=True)  # Link untuk melamar
    apply_email = models.EmailField(blank=True, null=True)  # Email untuk melamar

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-posted_at']  # Urutkan berdasarkan tanggal posting secara descending

    def save(self, *args, **kwargs):
        # Automatically generate slug from the title if it's not already set
        if not self.slug:
            self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def time_since_posted(self):
        return self._custom_timesince(self.posted_at) + " yang lalu"

    def time_until_expiration(self):
        if self.expiration_date:
            now = timezone.now()
            if self.expiration_date > now:
                return self._custom_timesince(now, self.expiration_date) + " lagi"
            else:
                return "Kadaluarsa"
        return "Tidak ada tanggal kadaluarsa"

    def _custom_timesince(self, d, now=None):
        """
        Mengembalikan waktu relatif dalam format yang disesuaikan.
        """
        if now is None:
            now = timezone.now()
        delta = now - d

        if delta.days >= 365:
            years = delta.days // 365
            return f"{years} tahun"
        elif delta.days >= 30:
            months = delta.days // 30
            return f"{months} bulan"
        elif delta.days >= 7:
            weeks = delta.days // 7
            return f"{weeks} minggu"
        elif delta.days >= 1:
            return f"{delta.days} hari"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"{hours} jam"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"{minutes} menit"
        else:
            return f"{delta.seconds} detik"

    def _translate_timesince(self, timesince_str):
        translations = {
            'year': 'tahun',
            'years': 'tahun',
            'month': 'bulan',
            'months': 'bulan',
            'week': 'minggu',
            'weeks': 'minggu',
            'day': 'hari',
            'days': 'hari',
            'hour': 'jam',
            'hours': 'jam',
            'minute': 'menit',
            'minutes': 'menit',
            'second': 'detik',
            'seconds': 'detik',
        }
        for en, id in translations.items():
            timesince_str = timesince_str.replace(en, id)
        return timesince_str
