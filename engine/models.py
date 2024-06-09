from django.db import models

class proPermission(models.Model):
    permission = models.CharField(max_length=70, default="")

class proRoles(models.Model):
    role = models.CharField(max_length=70, default="")
    accessRoles = models.JSONField(default=dict, null=True, blank=True)
    permissionID = models.JSONField(default=list, null=True, blank=True)
    snippet = models.CharField(max_length=70, default="")

class proUsers(models.Model):
    firstName = models.CharField(max_length=70, default="")
    lastName = models.CharField(max_length=70, default="", null=True, blank=True)
    email = models.CharField(max_length=70, default="")
    empID = models.CharField(max_length=70, default="")
    roleID = models.ForeignKey(proRoles, on_delete=models.CASCADE)
    userName = models.CharField(max_length=70, default="", null=True, blank=True)
    password = models.CharField(max_length=255, default="", null=True, blank=True)
    activate = models.BooleanField(default=False)
    sessionID = models.CharField(max_length=255, default="", null=True, blank=True)
    sessionActivate = models.BooleanField(default=False)
    createdBy = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    createdDate = models.DateTimeField(auto_now_add=True)
