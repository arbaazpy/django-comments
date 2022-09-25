# Purpose
* Database optimization


## Installation
```
➜ python3 -m venv venv
➜ source venv/bin activate
(venv) ➜  pip install -r requirements.txt
(venv) ➜  python manage.py runserver
```

## Database Setup
```
➜ sudo -u postgres psql
postgres=# create database django_comments;
postgres=# create user comment_admin with encrypted password 'comment_admin';
postgres=# grant all privileges on database django_comments to comment_admin;
postgres=# \q
```


## Load data
```
python manage.py load_data
```

## Endpoints
`v2` shows optimized query endpoint.
```
http://127.0.0.1:8000/api/comments/
http://127.0.0.1:8000/api/v2/comments/
```
