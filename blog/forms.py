# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post, Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category',
                  'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Title Placeholder Area'}),
            'slug': forms.TextInput
            (attrs={'class': 'form-control',
                    'placeholder': 'Title tag Placeholder Area'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'elder',
                                             'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Title Placeholder Area'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput
            (attrs={'class': 'form-control',
                    'placeholder': 'Category Placeholder Area'}),
        }
