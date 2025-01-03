from django import template
import random

register = template.Library()

@register.filter
def insert_random(article_list, random_element):
    """
    Menyisipkan elemen tertentu ke posisi acak dalam daftar.
    """
    if not isinstance(article_list, list):
        return article_list
    position = random.randint(0, len(article_list))
    return article_list[:position] + [random_element] + article_list[position:]
