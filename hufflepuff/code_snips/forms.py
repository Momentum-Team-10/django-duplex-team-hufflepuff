from django import forms
from code_snips.models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'description',
            'text',
            'libraries',
            'language',
            'tags',
        ]
