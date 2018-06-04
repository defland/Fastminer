from django.db import models

class UserInfo(models.Model):
	ip = models.CharField(max_length=255)
	cpu = models.CharField(max_length=255)
	mem = models.CharField(max_length=255)
	mac = models.CharField(max_length=255)
	gpu = models.CharField(max_length=255)
	time_login = models.DateTimeField()