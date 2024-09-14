# isp_project/settings.py

import os
from pathlib import Path


LOGIN_URL = '/login/'  # Redirect users to the login page when not authenticated
LOGIN_REDIRECT_URL = '/dashboard/'  # Redirect users after login
LOGOUT_REDIRECT_URL = '/login/'



# BASE_DIR adalah direktori utama dari proyek
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Lokasi database SQLite
    }
}




# isp_project/settings.py

INSTALLED_APPS = [
    # Apps default Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'widget_tweaks',
    'crispy_bootstrap5',  # Ini untuk styling Bootstrap 5, tambahkan jika menggunakan Bootstrap 5


    # Tambahkan aplikasi lain
    'psb',
]




# isp_project/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Pastikan ini mengarah ke folder 'templates',  # Bisa diisi folder template khusus, jika ada
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# isp_project/settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# isp_project/settings.py

DEBUG = True  # Pengembangan lokal
ALLOWED_HOSTS = ['*']  # Terima semua host



# isp_project/settings.py

# URL yang akan digunakan untuk mengakses file statis di aplikasi web
STATIC_URL = '/static/'

# Tambahkan folder di mana Django mencari file statis (optional)
STATICFILES_DIRS = [BASE_DIR / 'static']  # Ini jika kamu memiliki file statis dalam folder 'static'


# isp_project/settings.py

ROOT_URLCONF = 'isp_project.urls'


# isp_project/settings.py

SECRET_KEY = 'Acs@12345'  # Contoh: 'your-unique-secret-key'

#CRISPY_TEMPLATE_PACK = 'bootstrap4'  # atau 'bootstrap5' jika menggunakan Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"







