# coding: utf-8
import hashlib, json, os, requests, uuid, traceback
FILE = '.jixueconfig.py'
DOMAIN = 'http://teamof.codes'
# DOMAIN = 'http://0.0.0.0:8000'
ACTIVE_API = '/activate/'


def enctypt(salt, raw_code):
	raw = hashlib.sha256(raw_code.encode('utf-8'))
	raw.update(salt.encode('utf-8'))
	key = raw.hexdigest()
	return key


def validate():
	# whether the file exists
	if not os.path.isfile(FILE):
		open(".jixueconfig.py","w+").close()

	# whether activated
	file_size = os.path.getsize(FILE)
	mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
					for ele in range(0,8*6,8)][::-1])
	
	if not file_size:
		serialcode = raw_input('请输入激活码：')
		origin_auth_key = requests.post(
			DOMAIN+ACTIVE_API, 
			data=json.dumps({
				"mac":mac,
				"serialcode": serialcode
			}))

		# whether the code is valid
		resp = json.loads(origin_auth_key.content)
		if origin_auth_key.status_code != 200:
			return 0, resp.get('FAILD')

		origin_auth_key = resp.get('SUCCESS')
		with open(FILE, 'w+') as file:
			file.write('%s:::%s' % (serialcode, origin_auth_key))
	else:
		try:
			with open(FILE, 'r+') as file:
				file_content = file.readlines()
				codes = file_content[0].split(':::')
				serialcode, origin_auth_key = codes
		except:
			return (0, traceback.format_exc())

	# validate the authkey
	salt = serialcode[2:9]
	auth_key = enctypt(salt=salt,
		raw_code=mac)
	if not auth_key == origin_auth_key:
		return 0, "文件已被篡改"
	else:
		return 1, "验证通过"

if __name__ == '__main__':
	status_code, tips = validate()
	if not status_code:
		print tips
	else:
		print "Let's rock！！"
