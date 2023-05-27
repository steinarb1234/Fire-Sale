from django import template

register = template.Library()

@register.filter
def truncate_name(value):
    max_length = 15
    if len(value) <= max_length:
        return value
    else:
        last_space_index = value[:max_length].rfind(' ')
        return value[:last_space_index]

register.filter('truncate_name', truncate_name)