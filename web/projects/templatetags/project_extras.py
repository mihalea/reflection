from django import template
import markdown
from django.utils.safestring import mark_safe
from mdx_gfm import GithubFlavoredMarkdownExtension

register = template.Library()


@register.filter(name="responsive", is_safe=True)
def responsive(text):
    html = text.replace("<img","<img class=\"img-responsive\" ")
    return mark_safe(html)

@register.filter()
def md(text):
    html = markdown.markdown(text, extensions=[GithubFlavoredMarkdownExtension()])
    return mark_safe(html)


