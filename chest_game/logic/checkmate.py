from chest_game.logic.move import Move
import copy

class CheckMate():
    def __init__(self, movement):
        self.movement = movement

    def check_after_move(self):
        colour = self.movement.whose_move()
        if not self.get_list_of_chessmans_attacking_king(colour):
            return True
        return False

    def get_list_of_chessmans_attacking_king(self, colour):
        list_of_chessmans = []
        if colour == 'Black':
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_black_chessmans():
                white_king = self.movement.get_chessboard().chessmanlist.get_white_king()
                move = Move(chessman.coordinates.get_field_name(), white_king.coordinates.get_field_name(), self.movement.get_chessboard())
                if self.movement.check_move(move):
                    list_of_chessmans.append(chessman)
        else:
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_white_chessmans():
                black_king = self.movement.get_chessboard().chessmanlist.get_black_king()
                move = Move(chessman.coordinates.get_field_name(), black_king.coordinates.get_field_name(), self.movement.get_chessboard())
                if self.movement.check_move(move):
                    list_of_chessmans.append(chessman)
        return list_of_chessmans
    
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
                print([x_diff, y_diff])
                coordinates_to_check = copy.deepcopy(king.coordinates)
                if coordinates_to_check.change_coordinates([x_diff, y_diff]):
                    print('xx' + coordinates_to_check.get_field_name())
                    move = Move(king.coordinates.get_field_name(), coordinates_to_check.get_field_name(), self.movement.get_chessboard())
                    if self.movement.check_move_to_mate(move):
                        list_of_coordinates.append(coordinates_to_check)
        for x in list_of_coordinates:
            print(x.get_field_name())
        return list_of_coordinates