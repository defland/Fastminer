from django.contrib import admin
from .models import Coin, GPU, MiningPool

admin.site.register(Coin)
admin.site.register(GPU)
admin.site.register(MiningPool)
