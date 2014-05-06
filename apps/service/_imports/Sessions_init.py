#! Sessions
#! Django Sessions and Authentications
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.contrib.auth import logout
