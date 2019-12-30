from collections import defaultdict
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape
from django.utils.safestring import mark_safe, SafeData

from ..models import Smile

register = template.Library()


@register.filter
def list_commas(obj_list):
    if not obj_list:
        return ''
    return ', '.join(obj_list)


@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def show_smile(value, autoescape=None):
    autoescape = autoescape and not isinstance(value, SafeData)
    if autoescape:
        value = escape(value)
    index_dict = defaultdict(list)
    img_tag = '<img src="{}">'

    # разделим строку на слова
    words = value.split()

    # наполним словарь словами
    for word_index in range(len(words)):
        index_dict[words[word_index]].append(word_index)

    # найдем все смайлы из текста
    smiles = Smile.objects.filter(code__in=words)

    # заменим картинками текстовые смайлы
    for smile in smiles:
        word_index_replaces = index_dict[smile.code]
        for index in word_index_replaces:
            words[index] = img_tag.format(smile.smile.url)

    return mark_safe(' '.join(words))
