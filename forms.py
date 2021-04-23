from django import forms
from . import models


class createform(forms.ModelForm):
    class Meta:
        model = models.STATE
        fields = ('title', 'slug', 'body', 'image')
