# Generated by Django 4.2.3 on 2023-08-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_banner_options_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
