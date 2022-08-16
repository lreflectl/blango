from django import template
from django.contrib.auth import get_user_model
# from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html


user_model = get_user_model()
register = template.Library()


# @register.filter(name="author_details")
@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    return ''

  if author == current_user:
    return mark_safe('<strong>me</strong>')

  if author.first_name and author.last_name:
    name = f'{author.first_name} {author.last_name}'
  else:
    name = author.username
  
  if author.email:
    # Automatically escape arguments inserted in html and mark it as safe
    name = format_html(
      '<a href="mailto:{}">{}</a>',
      author.email,
      name,
    )

  return name
