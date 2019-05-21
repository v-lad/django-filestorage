from django import template

register = template.Library()

@register.filter
def get_filename(fn):
    return fn[fn.rfind('/')+1:]