# Generated by Django 3.2.12 on 2024-06-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0018_projecttask'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='projectNumber',
            field=models.CharField(default='', max_length=10),
        ),
    ]
