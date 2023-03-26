from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 21})
    )

    class Meta:
        model = Post
        fields = ('image', 'description',)
