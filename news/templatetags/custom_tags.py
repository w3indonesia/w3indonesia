from django import template
import random

register = template.Library()

@register.filter
def insert_random(value, insertion):
    """
    Sisipkan 'insertion' ke dalam list 'value' di posisi acak.
    """
    if not isinstance(value, list):
        return value
    
    if len(value) == 0:
        return [insertion]
    
    # Tentukan posisi acak
    random_index = random.randint(0, len(value))
    return value[:random_index] + [insertion] + value[random_index:]
