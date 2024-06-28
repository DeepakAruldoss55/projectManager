# Generated by Django 3.2.12 on 2024-06-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_projectStatusData'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectTaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=70, null=True)),
                ('technicalName', models.CharField(blank=True, default='', max_length=70, null=True)),
            ],
        ),
    ]