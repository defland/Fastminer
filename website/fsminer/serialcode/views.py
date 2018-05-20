from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import SerialCode

import hashlib, json

def enctypt(salt, raw_code):
	raw = hashlib.sha256(raw_code.encode('utf-8'))
	raw.update(salt.encode('utf-8'))
	key = raw.hexdigest()
	return key

@require_http_methods(["POST"])
def activate_code(request):
	received_json_data=json.loads(request.body.decode('utf-8'))
	mac = received_json_data.get('mac')
	serialcode = received_json_data.get('serialcode')

	# validate the request data
	if not (mac and serialcode):
		return JsonResponse({"ACTIVATE FAILD":"Invalid data"}, status=400)

	# If the code exist & not activated
	serialcode = SerialCode.objects.get(serialcode=serialcode)
	if serialcode:
		auth_key = serialcode.auth_key
		if auth_key:
			return JsonResponse({"ACTIVATE FAILD":"already activated"}, status=400)
	else:
		return JsonResponse({"ACTIVATE FAILD":"Invalid code"}, status=400)

	# activate & save key
	salt = serialcode.serialcode[2:9]
	auth_key = enctypt(salt=salt, raw_code=mac)
	serialcode.mac = mac
	serialcode.auth_key = auth_key
	serialcode.save()

	return JsonResponse({"SUCCESS":serialcode.auth_key}, status=200)

