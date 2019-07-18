import random
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def add_random_number(text):
    return f'{text}  {random.randint(1, 10)}'


@register.simple_tag
def select_description(article, language=''):
    if language and language != 'uk':
        return mark_safe(getattr(article, 'description_{}'.format(language)))
    else:
        return mark_safe(article.description)
