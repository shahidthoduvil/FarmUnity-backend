# Generated by Django 4.2.3 on 2023-07-13 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_rename_is_superadmin_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Occup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.occupation'),
        ),
    ]
