from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.CharField(
        verbose_name='Описание',
        null=False,
        max_length=200
    )
    image = models.ImageField(
        verbose_name='Фото',
        null=False,
        blank=True,
        upload_to='posts'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='posts',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    comments_count = models.IntegerField(
        verbose_name='Количество комментариев',
        default=0,
    )
    likes_count = models.IntegerField(
        verbose_name='Количество лайков',
        default=0,
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.description}"


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        verbose_name='Публикация',
        to='posts.Post',
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='Комментарий',
        null=False,
        blank=False,
        max_length=200
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"{self.text}"
