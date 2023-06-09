# Generated by Django 4.1.7 on 2023-04-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_created_at_account_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='about_me',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Информация о пользователе'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Номер телефона'),
        ),
    ]
