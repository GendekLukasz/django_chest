from chest_game.logic.field import Field
from chest_game.logic.chessboard import Chessboard

class Movement():
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.number_of_moves = 0

    def move(self, from_fied, to_field):
        if self.check_coordinates_on_board(to_field):
            chessman_to_move = self.chessboard.board[from_fied[0]][from_fied[1]].get_chessman()
            if self.whose_move() == chessman_to_move.get_colour():
                if chessman_to_move.check_move(from_fied, to_field):
                    self.chessboard.board[from_fied[0]][from_fied[1]].delete_chessman()
                    chessman_to_move.add_move()
                    self.add_move()
                    self.chessboard.board[to_field[0]][to_field[1]].set_chessman(chessman_to_move)

    def check_coordinates_on_board(self, coordinates):
        if coordinates[0] >= 0 and coordinates[0] <= 7 and coordinates[1] >= 0 and coordinates[1] <= 7:
            return True
        else:
            return False

    def add_move(self):
        self.number_of_moves =+ 1

    def whose_move(self):
        if self.number_of_moves%2 == 0:
            return "White"
        else:
            return "Black"