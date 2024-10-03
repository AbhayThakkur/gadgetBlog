from django import template

register = template.Library()

@register.filter
def dict_has_key(dictionary, key):
    """Check if the key exists in the dictionary."""
    return key in dictionary
