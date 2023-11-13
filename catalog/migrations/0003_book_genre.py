# Generated by Django 4.2.6 on 2023-10-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_alter_author_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.genre'),
        ),
    ]
