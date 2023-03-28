from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 21})
    )

    class Meta:
        model = Post
        fields = ('image', 'description',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
