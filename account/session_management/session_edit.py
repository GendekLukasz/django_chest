from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from . import session_data

def add_data_to_user_session(id, data_name, data):
    session = session_data.get_active_session_by_user_id(id)
    print(id)
    s = SessionStore(session_key=session.session_key)
    s[data_name] = data
    print(s[data_name])
    s.save()
    s.modified