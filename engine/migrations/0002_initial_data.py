from django.db import migrations
from django.utils import timezone
from django.contrib.auth.hashers import make_password

def create_basic_data(apps, schema_editor):
    proPermission = apps.get_model('engine', 'proPermission')
    proRoles = apps.get_model('engine', 'proRoles')
    proUsers = apps.get_model('engine', 'proUsers')

    # Create permissions
    read = proPermission.objects.create(permission='read')
    write = proPermission.objects.create(permission='write')

    # Create roles
    superadmin_role = proRoles.objects.create(
        role='superAdmin',
        accessRoles=[2, 3, 4, 5],
        permissionID=[read.id, write.id],
        snippet='Super Admin'
    )
    admin_role = proRoles.objects.create(
        role='admin',
        accessRoles=[3, 4, 5],
        permissionID=[read.id, write.id],
        snippet='Admin'
    )
    manager_role = proRoles.objects.create(
        role='manager',
        accessRoles=[4, 5],
        permissionID=[read.id, write.id],
        snippet='Manager'
    )
    employee_role = proRoles.objects.create(
        role='employee',
        accessRoles=None,
        permissionID=[read.id, write.id],
        snippet='Employee'
    )
    guest_role = proRoles.objects.create(
        role='guest',
        accessRoles=None,
        permissionID=[read.id],
        snippet='Guest'
    )

    # Create user
    proUsers.objects.create(
        firstName='Deepak',
        lastName='Aruldoss',
        email='adeepakplm55@gmail.com',
        empID='BC1011',
        userName='admin',
        password=make_password('admin@123'),
        roleID=superadmin_role,
        activate=True,
        sessionActivate=True,
        createdBy=None,
        createdDate=timezone.now()
    )

class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial_table'),
    ]

    operations = [
        migrations.RunPython(create_basic_data),
    ]
