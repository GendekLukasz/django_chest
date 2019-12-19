from chest_game.logic.field import Field
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.coordinates import Coordinates

class Move():
    def __init__(self, from_coor, to_coor, chessboard):
        self.from_coor = Coordinates(from_coor)
        self.to_coor = Coordinates(to_coor)
        self.chessman_to_move = chessboard.get_chessman(self.from_coor)
        self.chessman_to_attack = chessboard.get_chessman(self.to_coor)
        self.absolute_value = self.from_coor.get_absolute_value(self.to_coor)
        self.board = chessboard
        self.attack = False
    
    def get_from_coor(self):
        return self.from_coor
    
    def get_to_coor(self):
        return self.to_coor
    
    def get_chessman_to_move(self):
        return self.chessman_to_move
    
    def get_chessman_to_attack(self):
        return self.chessman_to_attack
    
    def get_absolute_value(self):
        return self.absolute_value
    
    def get_chessboard(self):
        return self.board

    def check_its_attack(self):
        if self.chessman_to_attack == None:
            return False
        else:
            return True

    def set_attack(self):
        self.attack = True

    def check_its_attack_on_opponent(self):
        return self.attack

    def get_rook_to_castling(self):
        absolute = self.get_absolute_value()
        if self.from_coor.get_field_name() == 'e1':
            if absolute[0] == 2:
                return self.board.board[7][7].get_chessman()
            elif absolute[0] == -2:
                return self.board.board[7][0].get_chessman()
        if self.from_coor.get_field_name() == 'e8':
            if absolute[0] == 2:
                return self.board.board[0][7].get_chessman()
            elif absolute[0] == -2:
                return self.board.board[0][0].get_chessman()
        return None
        
    def get_coor_to_check_before_castling(self):
        absolute = self.get_absolute_value()
        if self.from_coor.get_field_name() == 'e1':
            if absolute[0] == 2:
                return Coordinates('f1')
            elif absolute[0] == -2:
                return Coordinates('d1')
        if self.from_coor.get_field_name() == 'e8':
            if absolute[0] == 2:
                return Coordinates('f8')
            elif absolute[0] == -2:
                return Coordinates('f8')
        return None
