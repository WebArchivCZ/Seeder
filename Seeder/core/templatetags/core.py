from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def version():
    ''' Display the git-computed Seeder version '''
    return settings.VERSION


@register.simple_tag
def version_datetime():
    ''' Display the datetime of the last git commit '''
    return settings.VERSION_DATETIME
