# Generated by Django 5.0 on 2024-01-02 09:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]