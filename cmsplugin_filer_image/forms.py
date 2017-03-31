# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.forms import Textarea

from djangocms_attributes_field.widgets import AttributesWidget

from .models import FilerImage


class FilerImageForm(forms.ModelForm):

    class Meta:
        model = FilerImage
        exclude = []
        widgets = {
          'description': Textarea(attrs={'rows':2,}),
        }

    def __init__(self, *args, **kwargs):
        super(FilerImageForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()
