# Generated by Django 4.1.7 on 2024-02-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0013_alter_lead_divisional_operations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='business_verticals',
            field=models.CharField(blank=True, default='trading', max_length=255),
        ),
        migrations.AlterField(
            model_name='lead',
            name='divisional_operations',
            field=models.CharField(blank=True, default='hh', max_length=255),
        ),
    ]
