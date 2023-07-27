# Generated by Django 4.2.3 on 2023-07-27 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0003_member_is_list_quote_is_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Member'},
        ),
        migrations.AlterModelOptions(
            name='quote',
            options={'verbose_name': 'Quote'},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]