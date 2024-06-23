# Generated by Django 3.2.12 on 2024-06-23 02:42

from django.db import migrations

def billingTypeData(apps, schema_editor):
    billingType = apps.get_model('engine', 'billingType')

    none = billingType.objects.create(
        name='None',
        technicalName='none'
    )

    billable = billingType.objects.create(
        name='Billable',
        technicalName='billable'
    )

    nonbillable = billingType.objects.create(
        name='Non Billable',
        technicalName='nonbillable'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0013_billingType'),
    ]

    operations = [
        migrations.RunPython(billingTypeData),
    ]
