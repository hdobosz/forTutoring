- connect postgreSQL db
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myblogdb', #example
        'USER': 'postgres', #example
        'PASSWORD': '123456', #example
        'HOST': 'localhost', #example
        'PORT': '5432',
    }
}
```

