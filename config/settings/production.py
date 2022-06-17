from .base import *  # noqa
# from .base import env


DEBUG = env.bool("DJANGO_DEBUG", False)
SET_DEV = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS_PROD", default=[])

print(' + end_config PRODUCTION')