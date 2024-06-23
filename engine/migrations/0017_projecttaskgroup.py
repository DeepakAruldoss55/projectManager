# Generated by Django 3.2.12 on 2024-06-23 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0016_priorityTypeData'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectTaskGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskGroup', models.CharField(default='', max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_groups', to='engine.prousers')),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.projects')),
            ],
        ),
    ]