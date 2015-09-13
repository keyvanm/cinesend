from django import template
from django.contrib.flatpages.models import FlatPage
from django.template.loader import render_to_string
import markdown_deux

register = template.Library()


@register.simple_tag
def load_flat_page_content(flatpage_url, template_name=None):
    try:
        return markdown_deux.markdown(FlatPage.objects.get(url=flatpage_url).content, "trusted")
    except FlatPage.DoesNotExist:
        if template_name:
            return render_to_string(template_name)
        return ""

