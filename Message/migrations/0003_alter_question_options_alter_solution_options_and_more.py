# Generated by Django 4.2.3 on 2023-08-15 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Message', '0002_solution_delete_soluton'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question'},
        ),
        migrations.AlterModelOptions(
            name='solution',
            options={'verbose_name': 'Solution'},
        ),
        migrations.AddField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
