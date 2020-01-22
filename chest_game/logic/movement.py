from chest_game.logic.field import Field
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.coordinates import Coordinates
from chest_game.logic.checkmate import CheckMate
from chest_game.logic.move import Move
import copy

class Movement():
    def __init__(self, chessboard):
        self.castling = False
        self.chessboard = chessboard
        self.number_of_moves = 0

    def get_chessboard(self):
        return self.chessboard

    def move(self, move):
        if self.check_move(move):
            if self.check_after_move(move):
                self.move_chessman(move)
                print('xxx1')
                self.check_mate_after_move()

    def check_move(self, move):
        return self.check_field_is_empty(move) and self.check_good_colour_move(move) and self.check_attack_on_opponent(move) and self.check_collison_and_direct(move) and self.check_castling(move)

    def check_move_without_colour(self, move):
        return self.check_field_is_empty(move) and self.check_attack_on_opponent(move) and self.check_collison_and_direct(move) 

    def check_move_to_mate(self, move):
        return self.check_move_without_colour(move) and self.check_after_move(move)

    def check_mate_after_move(self):
        checkmate = CheckMate(copy.deepcopy(self))
        if checkmate.check_mate_after_move():
            return True
        else:
            self.chessboard.mate_by = self.who_defend()
            return False

    def check_after_move(self, move):
        checkmate = CheckMate(copy.deepcopy(self))
        checkmate.movement.move_chessman(move)
        if checkmate.check_after_move():
            return True
        else:
            self.chessboard.error.add_error('Ruch niedozwolony, groźba szacha.')
            return False

    def check_castling(self, move):
        if self.check_its_castling(move):
            if self.check_king_and_rook(move):
                if self.check_fields_beetwen_king_and_rook(move):
                    if self.starting_check_before_castling(move):
                        if self.middle_check_before_castling(move):
                            self.castling = True
                            return True
                        else:
                            self.chessboard.error.add_error('Szach pośredni.')
                            return False

                    else:
                        self.chessboard.error.add_error('Roszada niedozwolona, przy szachu.')
                        return False
                else:
                    self.chessboard.error.add_error('Przeszkoda')
                    return False
            else:
                self.chessboard.error.add_error('Roszada niemożliwa.')
                return False
        return True
        
    def check_its_castling(self, move):    
        chessman_to_move = move.get_chessman_to_move()
        if chessman_to_move.get_name() == 'King':
            if chessman_to_move.get_castling():
                    return True
        return False

    def starting_check_before_castling(self, move):
        chessman_to_move = move.get_chessman_to_move()
        move = Move(chessman_to_move.coordinates.get_field_name(), chessman_to_move.coordinates.get_field_name(), self.get_chessboard())
        if self.check_after_move(move):
            return True
        return False
    
    def middle_check_before_castling(self, move):
        chessman_to_move = move.get_chessman_to_move()
        move = Move(chessman_to_move.coordinates.get_field_name(), move.get_coor_to_check_before_castling().get_field_name(), self.get_chessboard())
        if self.check_after_move(move):
            return True
        return False

    def check_king_and_rook(self, move):
        chessman_to_move = move.get_chessman_to_move()
        rook = move.get_rook_to_castling()
        if rook != None:
            if chessman_to_move.get_number_of_moves() == 0 and rook.get_number_of_moves() == 0:
                return True
        return False

    def check_fields_beetwen_king_and_rook(self, move):
        chessman_to_move = move.get_chessman_to_move()
        rook = move.get_rook_to_castling()
        if rook.check_move_collision(Move(rook.coordinates.get_field_name(), chessman_to_move.coordinates.get_field_name(), self.get_chessboard())):
            return True
        else:
            return False

    def move_chessman(self, move):
        self.chessboard.get_field(move.get_to_coor()).set_chessman(move.get_chessman_to_move())
        if move.get_to_coor().get_field_name() != move.get_from_coor().get_field_name():
            self.chessboard.get_field(move.get_from_coor()).delete_chessman()
            self.chessboard.chessmanlist.delete_chessman_from_list(move.get_to_coor())
            self.chessboard.chessmanlist.update_coordinates_by_move(move)
        self.chessboard.get_chessman(move.get_to_coor()).add_move()
        if self.castling:
            rook_move = Move(move.get_rook_to_castling().coordinates.get_field_name(), move.get_coor_to_check_before_castling().get_field_name(), self.get_chessboard())
            self.chessboard.get_field(rook_move.get_to_coor()).set_chessman(rook_move.get_chessman_to_move())
            self.chessboard.get_field(rook_move.get_from_coor()).delete_chessman()
            self.chessboard.chessmanlist.delete_chessman_from_list(rook_move.get_to_coor())
            self.chessboard.chessmanlist.update_coordinates_by_move(rook_move)
            self.castling = False
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
        if self.number_of_moves != 0 and self.number_of_moves%2 != 0:
            return "Black"
        else:
            return "White"

    def who_defend(self):
        if self.number_of_moves != 0 and self.number_of_moves%2 != 0:
            return "White"
        else:
            return "Black"

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