# Generated by Django 4.2.3 on 2023-08-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_remove_post_comment_count_remove_post_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
