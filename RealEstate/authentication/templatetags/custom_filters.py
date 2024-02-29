from django import template

register = template.Library()

@register.filter
def format_field_name(value):
    return value.capitalize().replace('_', ' ')
