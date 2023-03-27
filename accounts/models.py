from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


class GenderChoices(TextChoices):
    MAN = 'Мужской', 'Мужской'
    WOMAN = 'Женский', 'Женский'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=True,
        null=False,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    about_me = models.TextField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name='Информация о пользователе'
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=12,
        null=True,
        blank=True
    )
    sex = models.CharField(
        choices=GenderChoices.choices,
        verbose_name='Пол',
        null=True,
        blank=True,
        max_length=50,
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='posts.Post',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers'
    )
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='posts.Post',
        related_name='user_comments'
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.email} - {self.username}"
