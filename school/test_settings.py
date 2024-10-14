from school.settings import *

# Custom settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL backend
        'NAME': 'test_electo_db',  # Database name
        'USER': 'postgres',  # Username
        'PASSWORD': 'postgres',  # Your password (replace with the actual password)
        'HOST': 'localhost',  # Database host
        'PORT': '5432',  # Database port
    }
}
