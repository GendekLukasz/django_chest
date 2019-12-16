from chest_game.logic.move import Move
from chest_game.logic.coordinates import Coordinates
import copy

class CheckMate():
    def __init__(self, movement):
        self.movement = movement

    def check_after_move(self):
        colour = self.movement.whose_move()
        if not self.get_list_of_chessmans_attacking_king(colour):
            return True
        return False

    def check_mate_after_move(self):
        list_attacking_chessmans = self.get_list_of_chessmans_attacking_king(self.movement.who_defend())
        list_of_coordinates_to_escape = self.get_list_of_coordinates_where_king_can_move(self.movement.whose_move())
        list_of_coordinates_to_shield = self.get_list_of_coordinates_to_shield_king(list_attacking_chessmans, self.movement.whose_move())
        list_of_moves_to_shield = self.get_list_of_moves_to_sield_king(self.movement.whose_move(), list_of_coordinates_to_shield)

        if list_attacking_chessmans and not list_of_coordinates_to_escape and not list_of_moves_to_shield and not self.check_to_kill_attacking_chessman(self.movement.whose_move(), list_attacking_chessmans):
            return False
        else:
            return True

    def get_list_of_coordinates_to_shield_king(self, list_attacking_chessmans, colour):
        list_of_coordinates = []
        king = None
        if colour == 'White':
            king = self.movement.get_chessboard().chessmanlist.get_white_king()
        else:
            king = self.movement.get_chessboard().chessmanlist.get_black_king()
        for chessman in list_attacking_chessmans:
            move = Move(chessman.coordinates.get_field_name(), king.coordinates.get_field_name(), self.movement.get_chessboard())
            list_coor = chessman.get_list_of_coordinates_to_check_before_mate(move)
            if list_coor != None:
                for coor in list_coor:
                    tmp = Coordinates()
                    tmp.set_coordinates(coor)
                    list_of_coordinates.append(tmp)
        return list_of_coordinates

    def get_list_of_chessmans_attacking_king(self, colour):
        list_of_chessmans = []
        if colour == 'Black':
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_black_chessmans():
                white_king = self.movement.get_chessboard().chessmanlist.get_white_king()
                move = Move(chessman.coordinates.get_field_name(), white_king.coordinates.get_field_name(), self.movement.get_chessboard())
                if self.movement.check_move_without_colour(move):
                    list_of_chessmans.append(chessman)
        else:
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_white_chessmans():
                black_king = self.movement.get_chessboard().chessmanlist.get_black_king()
                move = Move(chessman.coordinates.get_field_name(), black_king.coordinates.get_field_name(), self.movement.get_chessboard())
                if self.movement.check_move_without_colour(move):
                    list_of_chessmans.append(chessman)
        return list_of_chessmans

    def check_to_kill_attacking_chessman(self, colour, list_attacking_chessmans):
        list_of_chessmans = []
        moves = 0
        for l in list_attacking_chessmans:
            moves += 1
            if moves > 1:
                return False
        if colour == 'Black':
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_black_chessmans():
                for attacking_chessman in list_attacking_chessmans:
                    move = Move(chessman.coordinates.get_field_name(), attacking_chessman.coordinates.get_field_name(), self.movement.get_chessboard())
                    if self.movement.check_move_to_mate(move):
                        return True
        else:
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_white_chessmans():
                for attacking_chessman in list_attacking_chessmans:
                    move = Move(chessman.coordinates.get_field_name(), attacking_chessman.coordinates.get_field_name(), self.movement.get_chessboard())
                    if self.movement.check_move_to_mate(move):
                        return True
        return False

    def get_list_of_moves_to_sield_king(self, colour, list_of_coordinates_to_shield):
        list_of_moves = []
        
        if colour == 'Black':
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_black_chessmans():
                for coor in list_of_coordinates_to_shield:
                    move = Move(chessman.coordinates.get_field_name(), coor.get_field_name(), self.movement.get_chessboard())
                    if self.movement.check_move_without_colour(move):
                        list_of_moves.append(move)
        else:
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_white_chessmans():
                for coor in list_of_coordinates_to_shield:
                    move = Move(chessman.coordinates.get_field_name(), coor.get_field_name(), self.movement.get_chessboard())
                    if self.movement.check_move_without_colour(move):
                        list_of_moves.append(move)
        return list_of_moves
    
    def get_list_of_coordinates_where_king_can_move(self, colour):
        list_of_moves = [1, 0 , -1]
        list_of_coordinates = []
        king = None
        if colour == 'White':
            king = self.movement.get_chessboard().chessmanlist.get_white_king()
        else:
            king = self.movement.get_chessboard().chessmanlist.get_black_king()
        for y_diff in list_of_moves:
            for x_diff in list_of_moves:
                coordinates_to_check = copy.deepcopy(king.coordinates)
                if coordinates_to_check.change_coordinates([x_diff, y_diff]):
                    move = Move(king.coordinates.get_field_name(), coordinates_to_check.get_field_name(), self.movement.get_chessboard())
                    if self.movement.check_move_to_mate(move):
                        list_of_coordinates.append(coordinates_to_check)
        return list_of_coordinates