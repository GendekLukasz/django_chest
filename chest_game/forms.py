from django import forms
from account.session_management import session_data

class StartGameForm(forms.Form):
    users = session_data.get_current_users()
    CHOISES = []
    CHOISES.append((str(0), 'Zagraj z AI'))
    for user in users:
        CHOISES.append((str(user.id), user.username))
    opponent = forms.ChoiceField(label = 'Wybierz użytkownika: ', choices = CHOISES)