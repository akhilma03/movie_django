# Generated by Django 4.1.3 on 2022-11-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_remove_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]