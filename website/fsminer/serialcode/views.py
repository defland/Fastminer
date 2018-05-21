from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import SerialCode

import hashlib, json, traceback

def enctypt(salt, raw_code):
	raw = hashlib.sha256(raw_code.encode('utf-8'))
	raw.update(salt.encode('utf-8'))
	key = raw.hexdigest()
	return key

@require_http_methods(["POST"])
def activate_code(request):
	try:
		received_json_data=json.loads(request.body.decode('utf-8'))
		mac = received_json_data.get('mac')
		serialcode = received_json_data.get('serialcode')

		# validate the request data
		if not (mac and serialcode):
			return JsonResponse({"FAILD":"Invalid data"}, status=400)

		# If the code exist & not activated
		try:
			serialcode = SerialCode.objects.get(serialcode=serialcode)
		except SerialCode.DoesNotExist:
			return JsonResponse({"FAILD":"Invalid code"}, status=400)

		auth_key = serialcode.auth_key
		if auth_key:
			return JsonResponse({"SUCCESS":serialcode.auth_key}, status=200)

		# activate & save key
		salt = serialcode.serialcode[2:9]
		auth_key = enctypt(salt=salt, raw_code=mac)
		serialcode.mac = mac
		serialcode.auth_key = auth_key
		serialcode.save()
	except Exception as e:
		print('GG----------:', traceback.format_exc())
		return JsonResponse({"FAILD":"server error"}, status=400)
	return JsonResponse({"SUCCESS":serialcode.auth_key}, status=200)

