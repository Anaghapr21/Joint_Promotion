# Generated by Django 4.1.7 on 2024-02-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_alter_lead_additional_notes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='lead_no',
        ),
    ]