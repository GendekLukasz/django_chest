from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from . import session_data

def add_data_to_user_session(id, data_name, data):
    session = session_data.get_active_session_by_user_id(id)
    s = SessionStore(session_key=session.session_key)
    s[data_name] = data
    s.save()
    s.modified

def delete_data_from_user_session(id, data_name):
    session = session_data.get_active_session_by_user_id(id)
    s = SessionStore(session_key=session.session_key)
    s[data_name] = None
    s.save()
    s.modified


def clear_sessions():
    Session.objects.all().delete()