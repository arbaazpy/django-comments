# Purpose:
* Database optimization


## Load data
```
python manage.py load_data
```

## Database Setup
```
➜ sudo -u postgres psql
postgres=# create database django_comments;
postgres=# create user comment_admin with encrypted password 'comment_admin';
postgres=# grant all privileges on database django_comments to comment_admin;
postgres=# \q
```