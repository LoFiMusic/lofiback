# Lofi Chanel API
###### Deployment Guide:

```bash
pip3 install -r requirements.txt
```
```bash
uwsgi --ini uwsgi.ini \\Production mode
python3 manage.py runserver \\Developer mode
```
```bash
DB_NAME_L=Database Name
DB_USER=Database User
DB_PASSWORD=Database Password
DB_HOST=Database Host
DB_PORT=Database Port
S_DEBUG=Debug True\False
```
Replase value lofiback/settings.py
```
SECRET_KEY = 'value_key'
```
