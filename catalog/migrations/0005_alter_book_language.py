# Generated by Django 4.2.6 on 2023-10-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Select a language', related_name='language', to='catalog.language'),
        ),
    ]
