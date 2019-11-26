from chest_game.logic.field import Field
from chest_game.logic.chessboard import Chessboard

class Movement():
    def __init__(self, chessboard):
        self.chessboard = chessboard

    def move(self, from_fied, to_field):
        chesmann_to_move = self.chessboard.board[from_fied[0]][from_fied[1]].delete_chessman()
        self.chessboard.board[to_field[0]][to_field[1]].set_chessman(chesmann_to_move)
