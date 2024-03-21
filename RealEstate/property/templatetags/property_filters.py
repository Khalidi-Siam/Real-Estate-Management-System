from django import template

register = template.Library()

@register.filter
def format_field_name(value):
    return value.capitalize().replace('_', ' ')

@register.filter
def get_type(value):
    """ It returns variable type as a pure string name """
    return type(value).__name__