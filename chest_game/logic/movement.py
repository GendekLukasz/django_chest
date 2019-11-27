from chest_game.logic.field import Field
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.coordinates import Coordinates

class Movement():
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.number_of_moves = 0

    def move(self, from_fied, to_field):
        chessman_to_move = self.chessboard.get_field(from_fied).get_chessman()
        if chessman_to_move != None and self.whose_move() == chessman_to_move.get_colour():
            if chessman_to_move.check_move(from_fied, to_field):
                self.chessboard.get_field(from_fied).delete_chessman()
                chessman_to_move.add_move()
                self.add_move()
                self.chessboard.get_field(to_field).set_chessman(chessman_to_move)
                
    def add_move(self):
        self.number_of_moves =+ 1

    def whose_move(self):
        if self.number_of_moves%2 == 0:
            return "White"
        else:
            return "Black"
