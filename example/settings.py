CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


DEBUG = True


INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "bulbs2",
    "example.app",
)


SECRET_KEY = "you'll never guess what my secret key is"


TIME_ZONE = "America/Chicago"


USE_TZ = True
