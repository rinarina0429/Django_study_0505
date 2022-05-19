from dataclasses import field
from django import forms
from .models import Romance, Comment

class RomanceForm(forms.ModelForm):
    class Meta:
        model=Romance
        fields=['title','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['username','comment_text']