from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Coin, GPU, MiningPool
import hashlib, json, traceback

def website(request):
    coins = Coin.objects.order_by('-calulation_ability')
    gpus = GPU.objects.order_by('-calculation')

    template = loader.get_template('website/index.html')
    context = {
        'coins': coins,
        'gpus': gpus,
    }
    return HttpResponse(template.render(context, request))


def get_miner_pool_api(request):
	try:
		resp = {}
		coins = Coin.objects.all()
		for coin in coins:
			print(coin.coin_en_name)
			resp[coin.coin_en_name] = {
				'coin_type': coin.coin_type,
				'calulation_ability': coin.calulation_ability,
				'earning_possibility': coin.earning_possibility,
				'coin_cn_name': coin.coin_cn_name,
				'coin_en_name': coin.coin_en_name,
				'coin_nickname': coin.coin_nickname,
				'coin_link': coin.coin_link,
				'pool':[]
			}
			pools = coin.coin_miningpool.all()
			for pool in pools:
				resp[coin.coin_en_name]['pool'].append({
						'pool': pool.pool,
						'miner': pool.miner,
						'url': pool.url,
						'hashrate': str(pool.hashrate) + 'GH/s',
						'blocks': pool.blocks,
						'last_blocks': pool.last_blocks.strftime('%Y-%m-%d %H:%M:%S'),
						'last_beat': pool.last_beat.strftime('%Y-%m-%d %H:%M:%S'),
						'difficulty':str(pool.difficulty) + 'T',
						'variance': str(pool.variance) + '%',
						'status': pool.status,
					})
		print(resp)
		return JsonResponse(resp, status=200)

	except Exception as e:
		print('GG----------:', traceback.format_exc())
		return JsonResponse({"FAILD":"server error"}, status=400)