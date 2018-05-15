from django import forms

class ArticleForm(forms.Form):
    title=forms.CharField(max_length=255,min_length=5)
    content=forms.CharField(min_length=10)