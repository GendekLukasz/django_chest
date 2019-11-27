from chest_game.logic.field import Field
from chest_game.logic.coordinates import Coordinates
from chest_game.logic.chessmans.pawn import Pawn
from chest_game.logic.chessmans.bishop import Bishop
from chest_game.logic.chessmans.king import King
from chest_game.logic.chessmans.knight import Knight
from chest_game.logic.chessmans.queen import Queen
from chest_game.logic.chessmans.rook import Rook

class Chessboard():

    def __init__(self):
        self.board = []
        self.fill_board_with_rows()
        self.chessborad_starting_point()

    def fill_board_with_rows(self):
        for y in range(1,9):
            if y%2 == 0:
                row = self.fill_row_with_fields(True)
                self.board.append(row)
            else:
                row = self.fill_row_with_fields(False)
                self.board.append(row)
            
    def fill_row_with_fields(self,even):
        row = []
        for x in range(1,9):
            if even:
                if x%2 == 0:
                    field = Field('grey')
                    row.append(field)
                else:
                    field = Field('brown')
                    row.append(field)  
            else:
                if x%2 == 0:
                    field = Field('brown')
                    row.append(field)
                else:
                    field = Field('grey')
                    row.append(field)  
        return row

    def fill_chessborad_with_chessman(self, chessman):
        chesman_list = chessman.get_starting_points_list()
        for coordinates in chesman_list['black']:
            chess = chessman(chessman.__name__, "Black")
            self.board[coordinates[0]][coordinates[1]].set_chessman(chess)
            
        for coordinates in chesman_list['white']:
            chess = chessman(chessman.__name__, "White")
            self.board[coordinates[0]][coordinates[1]].set_chessman(chess)

    def chessborad_starting_point(self):
        chessmans_list = [Pawn, Bishop, Rook, Queen, King, Knight]
        for t in chessmans_list:
            self.fill_chessborad_with_chessman(t)

    def get_field(self, coordinates):
        return self.board[coordinates.get_x()][coordinates.get_y()]
