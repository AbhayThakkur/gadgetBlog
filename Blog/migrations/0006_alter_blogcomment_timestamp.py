# Generated by Django 5.1 on 2024-09-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
