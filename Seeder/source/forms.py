import models

from django import forms
from django.forms.models import modelformset_factory
from django.forms.formsets import BaseFormSet
from django.utils.translation import ugettext as _


source_fields = (
    'name', 'publisher', 'frequency', 'special_contact', 'conspectus',
    'sub_conspectus', 'web_proposal', 'open_license', 'comment')


class SourceForm(forms.ModelForm):
    open_license = forms.BooleanField(
        required=False,
        help_text=_('Is text distributed under open license?')
    )

    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}),
                              required=False)

    class Meta:
        model = models.Source
        fields = source_fields


class ManagementSourceForm(SourceForm):
    """
    This is pretty much the same as SourceForm with the difference that it
    allows to select owner=curator of the source.
    """

    class Meta:
        model = models.Source
        fields = ('owner',) + source_fields


class BaseSeedFormset(BaseFormSet):
    def clean(self):
        """
        Checks that there is always at least one valid seed
        """
        urls = [frm.cleaned_data.get('url', None) for frm in self.forms]
        if not any(urls):
            raise forms.ValidationError(_('There must be at least one seed!'))

SeedFormset = modelformset_factory(models.Seed, fields=('url',), extra=1,
                                   formset=BaseSeedFormset)
