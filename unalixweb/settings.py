import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware"
]

ROOT_URLCONF = "unalixweb.urls"

INSTALLED_APPS = [
    "django.contrib.staticfiles"
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]

WSGI_APPLICATION = "unalixweb.wsgi.application"

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]