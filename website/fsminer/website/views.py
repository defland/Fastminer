from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Coin, GPU

def website(request):
    coins = Coin.objects.order_by('-calulation_ability')
    gpus = GPU.objects.order_by('-calculation')

    template = loader.get_template('website/index.html')
    context = {
        'coins': coins,
        'gpus': gpus,
    }
    return HttpResponse(template.render(context, request))