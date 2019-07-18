from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description')
        labels = {
            'title': 'Custom Title',
        }


class CommentsForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    object_id = forms.CharField(widget=forms.HiddenInput())
    model_name = forms.CharField(widget=forms.HiddenInput())
