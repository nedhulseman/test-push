from django import template

@register.filter(name='cut')
register = template.Library()
def cut(value, arg):
    return value.replace(arg, "")

#register.filter('cut', cut)
