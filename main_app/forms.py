from .models import Comment
from django.forms import ModelForm
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']