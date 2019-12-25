from django import template

register = template.Library()


@register.filter
def list_commas(obj_list):
    if not obj_list:
        return ''
    return ', '.join(obj_list)
