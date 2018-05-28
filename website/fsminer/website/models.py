from django.db import models

class Coin(models.Model):
	coin_type = models.CharField(max_length=64)
	calulation_ability = models.IntegerField(default=0)
	earning_possibility = models.CharField(max_length=255)
	coin_cn_name = models.CharField(max_length=1024)
	coin_en_name = models.CharField(max_length=1024)
	coin_nickname =  models.CharField(max_length=256)
	coin_link = models.CharField(max_length=2048)
	coin_3rd_id = models.IntegerField(default=1, null=False)

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

class MiningPool(models.Model):
	coin = models.ForeignKey(
		'Coin',
		on_delete=models.CASCADE,
		related_name='coin_miningpool'
	)
	url = models.CharField(max_length=2048)
	pool = models.CharField(max_length=256)
	miner = models.IntegerField()	
	hashrate = models.FloatField()
	blocks = models.FloatField()
	last_blocks = models.DateTimeField()
	last_beat = models.DateTimeField()
	difficulty = models.FloatField()
	variance =	models.FloatField()
	status = models.CharField(max_length=256)

	def __str__(self):
		return self.pool