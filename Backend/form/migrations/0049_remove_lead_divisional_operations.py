# Generated by Django 4.1.7 on 2024-03-01 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0048_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='divisional_operations',
        ),
    ]