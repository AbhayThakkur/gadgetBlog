# Generated by Django 5.1 on 2024-09-16 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='discription',
            new_name='description',
        ),
    ]
