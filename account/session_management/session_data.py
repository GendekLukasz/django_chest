from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=user_id_list)

def get_user_if_logged(user_id):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    for session in active_sessions:
        data = session.get_decoded()
        if data.get('_auth_user_id') == str(user_id):
            return User.objects.get(id=data.get('_auth_user_id'))

def get_active_session_by_user_id(user_id):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    session = []
    for session in active_sessions:
        if session.get_decoded().get('_auth_user_id') == str(user_id):
            return session