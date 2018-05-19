from django.db import models

class SerialCode(models.Model):
	serialcode = models.CharField(
		max_length=256,
		null=False,
		unique=True,
	)
	mac = models.CharField(
		max_length=64,
		null=True,
		blank=True,
	)
	auth_key = models.CharField(
		max_length=256,
		null=True,
		blank=True,
	)
	time_activated = models.DateTimeField(
		auto_now=True,
		null=True,
	)

	def __str__(self):
		return self.serialcode[:20]
