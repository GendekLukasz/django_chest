from chest_game.logic.move import Move

class CheckMate():
    def __init__(self, movement):
        self.movement = movement

    def check_after_move(self):
        colour = self.movement.whose_move()
        if colour == 'Black':
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_black_chessmans():

                white_king = self.movement.get_chessboard().chessmanlist.get_white_king()
                move = Move(chessman.coordinates.get_field_name(), white_king.coordinates.get_field_name(), self.movement.get_chessboard())
                if self.movement.check_move(move):
                    return False
        else:
            for chessman in self.movement.get_chessboard().chessmanlist.get_all_white_chessmans():
                black_king = self.movement.get_chessboard().chessmanlist.get_black_king()
                move = Move(chessman.coordinates.get_field_name(), black_king.coordinates.get_field_name(), self.movement.get_chessboard())
                if self.movement.check_move(move):
                    return False
        return True