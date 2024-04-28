# Generated by Django 4.1.7 on 2024-03-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('form', '0055_delete_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_no', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=255)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('company_headquarters', models.CharField(blank=True, max_length=255, null=True)),
                ('business_verticals', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_notes', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
