# -*- coding: utf-8 -*-
from django.conf import settings

USE_CAPTCHA = getattr(settings, 'GUESTBOOK_USE_CAPTCHA', True)
