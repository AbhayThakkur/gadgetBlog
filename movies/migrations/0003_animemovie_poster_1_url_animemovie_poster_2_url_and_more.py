# Generated by Django 5.1.4 on 2025-01-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_animemovie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='animemovie',
            name='poster_1_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animemovie',
            name='poster_2_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animemovie',
            name='poster_3_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animemovie',
            name='poster_1',
            field=models.ImageField(blank=True, null=True, upload_to='movies_posters/'),
        ),
        migrations.AlterField(
            model_name='animemovie',
            name='poster_2',
            field=models.ImageField(blank=True, null=True, upload_to='movies_posters/'),
        ),
        migrations.AlterField(
            model_name='animemovie',
            name='poster_3',
            field=models.ImageField(blank=True, null=True, upload_to='movies_posters/'),
        ),
    ]
