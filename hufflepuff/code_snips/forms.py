from django import forms
from code_snips.models import Comment, Snippet, Tag


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'description',
            'text',
            'language',
            'tags',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name',]