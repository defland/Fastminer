from django.shortcuts import render
from django.http import JsonResponse
from .models import UserInfo
import datetime, json

def userinfo(request):
	received_json_data=json.loads(request.body.decode('utf-8'))
	mac = received_json_data.get('mac')
	now = datetime.datetime.now()
	update_info = {
		'ip': received_json_data.get('ip'),
		'cpu': received_json_data.get('cpu'),
		'mem': received_json_data.get('mem'),
		'gpu': received_json_data.get('gpu'),
		'time_login':  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	}
	print(update_info)
	obj, created = UserInfo.objects.update_or_create(
		mac=mac,
		defaults=update_info,
	)
	response = json.dumps(update_info)
	return JsonResponse(response, status=201, safe=False)