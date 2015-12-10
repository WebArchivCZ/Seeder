import django_filters

from django.db import models
from core.widgets import RangeField


class EmptyFilter(django_filters.FilterSet):
    """
        Filter that filters based upon icontains lookup and allows empty choice
    """
    empty_choice = ('', '---------')
    filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }

    def __init__(self, *args, **kwargs):
        # pylint: disable=E1002
        super(EmptyFilter, self).__init__(*args, **kwargs)

        # add empty choice to all choice fields:
        is_choice = lambda f: isinstance(self.filters[f],
                                         django_filters.ChoiceFilter)
        choices = filter(is_choice, self.filters)

        for field_name in choices:
            extended_choices = ((self.empty_choice,) +
                                self.filters[field_name].extra['choices'])
            self.filters[field_name].extra['choices'] = extended_choices


class DateRangeFilter(django_filters.Filter):
    """
    Filter that has two fields and sets limits on the filter - it can be
    open range filter.
    """
    field_class = RangeField

    def filter(self, qs, value):
        date_from, date_to = value
        filter_queries = {}
        if date_from:
            filter_queries['{0}__gte'.format(self.name)] = date_from
        if date_to:
            filter_queries['{0}__lte'.format(self.name)] = date_to

        if filter_queries:
            return qs.filter(**filter_queries)
        return qs
