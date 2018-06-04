from django.contrib import admin
from .models import Coin, GPU, MiningPool, Version

admin.site.register(Coin)
admin.site.register(GPU)
admin.site.register(MiningPool)
admin.site.register(Version)
