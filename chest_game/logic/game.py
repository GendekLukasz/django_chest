import random
import string
from chest_game.logic.move import Move
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.movement import Movement
from account.session_management import session_game

class Game():
    def __init__(self, player1, player2):
        self.game_name = self.randomString() + '.game'
        self.chessboard = Chessboard()
        self.movement = Movement(self.chessboard)
        self.players = self.rand_colour([player1, player2])
        self.white_player = self.players['White']
        self.black_player = self.players['Black']
        self.winner = None
        session_game.new_game(self)

    def get_name(self):
        return self.game_name

    def rand_colour(self, players):
        white_player = random.choice(players)
        if players[1] is None:
            white_player = players[0]

        if players[0] == white_player:
            black_player = players[1]
        else:
            black_player = players[0]
        return {'White': white_player,
                'Black': black_player}

    def move(self, from_coor, to_coor, player):
        if self.check_good_player_move(player):
            if self.black_player is None:
                move = Move(from_coor, to_coor, self.movement.get_chessboard())
                self.movement.move(move)
                if not self.movement.chessboard.error.get_list_of_errors() and self.movement.chessboard.error.get_list_of_errors() != 'win':
                    self.random_move_for_bot()
                else:
                    return False
                return True
            else:
                move = Move(from_coor, to_coor, self.movement.get_chessboard())
                self.movement.move(move)
                return True
        else:
            return False
    
    
    def randomString(self, stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def random_move_for_bot(self):
        while True:
            m1 = Move(self.random_coor(), self.random_coor(), self.movement.get_chessboard())
            self.movement.move(m1)
            if not self.movement.chessboard.error.get_list_of_errors() or self.movement.chessboard.error.get_list_of_errors() == 'win':
                break

    def get_opponent_player(self, player):
        if self.black_player == None:
            return None
        if self.white_player.id == player.id:
            return black_player
        return self.white_player

    def check_good_player_move(self, player):
        id = 0
        if self.players[self.movement.whose_move()] is not None:
            id = self.players[self.movement.whose_move()].id

        if id == player.id:
            return True
        else:
            return False

    def random_coor(self):
        return random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) + random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])