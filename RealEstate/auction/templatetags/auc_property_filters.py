from django import template

register = template.Library()

@register.filter
def format_field_name(value):
    if value == "Block":
        value = "Block/Sector"
    else:
        value = value.capitalize().replace('_', ' ')
    return value

@register.filter
def get_type(value):
    """ It returns variable type as a pure string name """
    return type(value).__name__