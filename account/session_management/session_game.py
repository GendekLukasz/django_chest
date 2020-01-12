import pickle
from account.session_management import session_data
from account.session_management import session_edit


def get_game(game_name):
    pickle_in = open(get_game_address(game_name), "rb")
    game = pickle.load(pickle_in)
    pickle_in.close()
    return game

def save_game(game):
    game_name = game.get_name()
    pickle_out = open(get_game_address(game_name), "wb")
    pickle.dump(game, pickle_out)
    pickle_out.close()

def new_game(game):
    game_name = game.get_name()
    pickle_out = open(get_game_address(game_name), "wb")
    pickle.dump(game, pickle_out)
    pickle_out.close()
    connect_game_with_players_by_session(game)

def connect_game_with_players_by_session(game):
    game_name = game.get_name()
    p1 = game.white_player.id
    p2 = game.black_player.id

    if p1 != 0:
        session_edit.add_data_to_user_session(p1, 'game', game_name)
    
    if p2 != 0:
        session_edit.add_data_to_user_session(p2, 'game', game_name)
        
def get_game_address(game_name):
    return 'games/' + game_name