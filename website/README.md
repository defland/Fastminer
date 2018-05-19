```bash
virtualenv -p python3 3env
source 3env/bin/activate
pip install -r req.txt
cd fsminer
python manage.py createsuperuser(for admin)
python manage.py runserver(debug)
```

# Admin
http://127.0.0.1:8000/admin/website/
http://127.0.0.1:8000/website/


# Gunicorn
```bash
whereis gunicorn
cd xxx/Fastminer/website/fsminer
xxx/Fastminer/website/3env/bin/gunicorn fsminer.wsgi:application -w 3 -b 0.0.0.0:8000
```
