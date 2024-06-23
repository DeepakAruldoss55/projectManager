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

class projectStatus(models.Model):
    name = models.CharField(max_length=70, default="", null=True, blank=True)
    technicalName = models.CharField(max_length=70, default="", null=True, blank=True)

class projectTaskStatus(models.Model):
    name = models.CharField(max_length=70, default="", null=True, blank=True)
    technicalName = models.CharField(max_length=70, default="", null=True, blank=True)

class clients(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.CharField(max_length=255, default="", null=True, blank=True)
    email = models.CharField(max_length=200, default="", null=True, blank=True)
    mobile = models.CharField(max_length=30, default="", null=True, blank=True)
    address = models.CharField(max_length=255, default="", null=True, blank=True)
    createdBy = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_clients')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_clients')
    updatedDate = models.DateTimeField(null=True, blank=True)

class projects(models.Model):
    projectNumber = models.CharField(max_length=10, default="")
    name = models.CharField(max_length=255, default="")
    projectStatusID = models.ForeignKey(projectStatus, null=True, blank=True, on_delete=models.PROTECT)
    clientID = models.ForeignKey(clients, null=True, blank=True, on_delete=models.PROTECT)
    createdBy = models.ForeignKey(proUsers, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_projects')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(proUsers, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_projects')
    updatedDate = models.DateTimeField(null=True, blank=True)

class billingType(models.Model):
    name = models.CharField(max_length=70, default="", null=True, blank=True)
    technicalName = models.CharField(max_length=70, default="", null=True, blank=True)

class priorityType(models.Model):
    name = models.CharField(max_length=70, default="", null=True, blank=True)
    technicalName = models.CharField(max_length=70, default="", null=True, blank=True)

class projectTaskGroup(models.Model):
    taskGroup = models.CharField(max_length=255, default="")
    projectID = models.ForeignKey(projects, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(proUsers, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_groups')
    createdDate = models.DateTimeField(auto_now_add=True)

class projectTask(models.Model):
    taskNumber = models.CharField(max_length=10, default="")
    taskName = models.CharField(max_length=255, default="")
    taskDescription = models.CharField(max_length=255, default="", null=True, blank=True)
    taskGroupID = models.ForeignKey(projectTaskGroup, on_delete=models.CASCADE)
    billingID = models.ForeignKey(billingType, on_delete=models.CASCADE)
    priorityID = models.ForeignKey(priorityType, on_delete=models.CASCADE)
    owners = models.JSONField(default=list, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endlineDate = models.DateField(null=True, blank=True)
    workHours = models.DurationField(null=True, blank=True)
    dueDate = models.DateField(null=True, blank=True)
    createdBy = models.ForeignKey(proUsers, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_tasks')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(proUsers, null=True, blank=True, on_delete=models.SET_NULL, related_name='updated_tasks')
    updatedDate = models.DateTimeField(null=True, blank=True)