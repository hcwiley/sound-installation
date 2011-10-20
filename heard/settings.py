# Django settings for doretax project.

import os
import sys
import socket

if 'blu-' in socket.gethostname():
    sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# root directories
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
GALLERY_ROOT = os.path.join(MEDIA_ROOT, 'gallery/')
AUDIO_ROOT = os.path.join(MEDIA_ROOT, 'sounds/')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected-static/')
# urls
MEDIA_URL = '/site_media/media/'
STATIC_URL = '/site_media/static/'
GALLERY_URL = '/gallery/'
AUDIO_URL = '/sounds/'


ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin/')
sys.path.append('%s/' % PROJECT_ROOT)
sys.path.append('%s/apps/' % PROJECT_ROOT)
sys.path.append('%s/apps/artist/' % PROJECT_ROOT)
sys.path.append('%s/apps/piece/' % PROJECT_ROOT)
 
ADMINS = (
    ('Cole Wiley', 'cole@decode72.com'),
    ('Zack Dever', 'zack@decode72.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'sounds.db'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xx6ew5*1z2b@$9t1jx*h2qlss9t85pvsq7ce=!#z)ugc)n&t4j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'heard.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
#    os.path.join(PROJECT_ROOT, 'templates/admin/'),
#    os.path.join(PROJECT_ROOT, 'templates/registration/'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static/'),
)

INSTALLED_APPS = (
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    # everything above needed for admin
    'django.contrib.localflavor',
    'django.contrib.staticfiles',
#    'south',
    'artist',
    'piece',
)

try:
    from local_settings import *
except ImportError:
    pass
