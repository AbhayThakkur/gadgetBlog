# Generated by Django 5.1.4 on 2025-01-05 08:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_post_image_url_alter_post_author_alter_post_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(help_text='Comment content'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Parent comment (for nested comments)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Blog.blogcomment'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(help_text='Post the comment is associated with', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blog.post'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Timestamp of the comment'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='user',
            field=models.ForeignKey(help_text='User who posted the comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
