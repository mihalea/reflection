from django import template
import re

register = template.Library()


@register.filter(name="responsive")
def responsive(text):
    return text.replace("<img","<img class=\"img-responsive\" ")

responsive.is_safe = True