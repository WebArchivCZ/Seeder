import operator

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Blacklist(models.Model):
    """
    General model for control lists

    There are two types of blacklists
    - blacklist that control Haritrex
    - visibility blacklists that control which pages can be accessed by visitor
    """
    TYPE_HARVEST = 0        # controls what gets harvested
    TYPE_VISIBILITY = 1     # controls what can be seen

    TYPE_CHOICES = (
        (TYPE_HARVEST, _('Haritrex blacklist')),
        (TYPE_VISIBILITY, _('Visibility blacklist')),
    )

    title = models.CharField(verbose_name=_('Title'), max_length=256)

    blacklist_type = models.IntegerField(
        choices=TYPE_CHOICES
    )

    url_list = models.TextField(
        verbose_name=_('List of urls to block')
    )

    class Meta:
        verbose_name = _('Blacklist')
        verbose_name_plural = _('Blacklists')
        ordering = ('id', )

    @classmethod
    def collect_urls_by_type(cls, blacklist_type):
        blacklist_urls = cls.objects.filter(
            blacklist_type=blacklist_type
        ).values_list('url_list', flat=True)
        # blacklist urls is now list of contents
        urls_parsed = map(unicode.splitlines, blacklist_urls)
        return reduce(operator.add, urls_parsed)
