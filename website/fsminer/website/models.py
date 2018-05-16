from django.db import models

class Coin(models.Model):
	coin_type = models.CharField(max_length=64)
	calulation_ability = models.IntegerField(default=0)
	earning_possibility = models.CharField(max_length=255)

	def __str__(self):
		return 'coin_type: %s' % self.coin_type

class GPU(models.Model):
	name = models.CharField(max_length=255)
	gtype = models.CharField(max_length=64)
	calculation = models.CharField(max_length=200)
	cost = models.CharField(max_length=255)
	day_earning = models.CharField(max_length=255)
	week_earning = models.CharField(max_length=255)
	month_earning = models.CharField(max_length=255)

	def __str__(self):
		return self.name