# Generated by Django 4.2.3 on 2023-07-27 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_alter_occupation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='Cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.category'),
        ),
    ]