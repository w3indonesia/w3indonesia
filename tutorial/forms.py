from django import forms
from .models import Subcategory

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = '__all__'

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if slug and Subcategory.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Slug harus unik.")
        return slug
