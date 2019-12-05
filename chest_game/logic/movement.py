from chest_game.logic.field import Field
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.coordinates import Coordinates

class Movement():
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.number_of_moves = 0

    def get_chessboard(self):
        return self.chessboard

    def move(self, move):
        if self.check_field_is_empty(move) and self.check_good_colour_move(move) and self.check_attack_on_opponent(move) and self.check_collison_and_direct(move):
            self.move_chessman(move)

    def move_chessman(self, move):
        self.chessboard.get_field(move.get_to_coor()).set_chessman(move.get_chessman_to_move())
        self.chessboard.get_field(move.get_from_coor()).delete_chessman()
        self.chessboard.get_chessman(move.get_to_coor()).add_move()
        self.add_move()
        self.chessboard.error.delete_errors()

    def add_move(self):
        self.number_of_moves += 1

    def check_field_is_empty(self, move):
        if move.get_chessman_to_move() == None:
            self.chessboard.error.add_error('Pole jest puste')
            return False
        else: 
            return True
    def check_good_colour_move(self, move):
        colour = self.whose_move()
        chessman = move.get_chessman_to_move()
        if chessman.get_colour() == colour:
            return True
        else:
            self.chessboard.error.add_error('To nie jest twój ruch.')
            return False

    def whose_move(self):
        if  self.number_of_moves != 0 and self.number_of_moves%2 != 0:
            return "Black"
        else:
            return "White"

    def check_attack_on_opponent(self, move):
        if move.check_its_attack():    
            if move.get_chessman_to_move().get_colour() == move.get_chessman_to_attack().get_colour():
                self.chessboard.error.add_error('Atak na swojego pionka.')
                return False
            else:
                move.set_attack()
                return True
        else:
            return True

    def check_collison_and_direct(self, move):
        chessman = move.get_chessman_to_move()
        if chessman.check_move(move) and chessman.check_move_collision(move):
            return True
        else:
            self.chessboard.error.add_error('Niedozwolony ruch.')
            return False