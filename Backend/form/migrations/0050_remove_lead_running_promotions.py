# Generated by Django 4.1.7 on 2024-03-01 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0049_remove_lead_divisional_operations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='running_promotions',
        ),
    ]
