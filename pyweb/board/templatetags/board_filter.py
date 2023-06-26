from django import template

register = template.Library()

@register.filter
def sub(valeu, arg):
    return valeu - arg  # 원래 값에서 - 매개값 -> |sub:arg