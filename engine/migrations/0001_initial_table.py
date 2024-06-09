# Generated by Django 3.2.12 on 2024-06-09 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='proRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='', max_length=70)),
                ('accessRoles', models.JSONField(blank=True, default=dict, null=True)),
                ('permissionID', models.JSONField(blank=True, default=list, null=True)),
                ('snippet', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='proUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=70)),
                ('lastName', models.CharField(blank=True, default='', max_length=70, null=True)),
                ('email', models.CharField(default='', max_length=70)),
                ('empID', models.CharField(default='', max_length=70)),
                ('userName', models.CharField(blank=True, default='', max_length=70, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('activate', models.BooleanField(default=False)),
                ('sessionID', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sessionActivate', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='engine.prousers')),
                ('roleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.proroles')),
            ],
        ),
    ]
