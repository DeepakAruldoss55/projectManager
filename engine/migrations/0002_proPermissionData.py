# Generated by Django 3.2.12 on 2024-06-22 12:57

from django.db import migrations

def proPermissionData(apps, schema_editor):
    proPermission = apps.get_model('engine', 'proPermission')

     # Create permissions
    read = proPermission.objects.create(permission='read')
    write = proPermission.objects.create(permission='write')

class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_proPermission'),
    ]

    operations = [
        migrations.RunPython(proPermissionData),
    ]
