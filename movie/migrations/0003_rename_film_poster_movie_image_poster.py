# Generated by Django 5.1.4 on 2025-01-20 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='film_poster',
            new_name='image_poster',
        ),
    ]
