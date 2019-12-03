from chest_game.logic.chessman import Chessman

class Rook(Chessman):
    def weight(self):
        return 1
        
    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[0,0], [0,7]],
            'white' : [[7,0], [7,7]],
        }

    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if absolute_value[0] == 0 or absolute_value[1] == 0:
            return True
        else :
            return False

    def check_move_collision(self, move):
        from_x = move.get_from_coor().get_x() if move.get_from_coor().get_x() <= move.get_to_coor().get_x() else move.get_to_coor().get_x()
        from_y = move.get_from_coor().get_y() if move.get_from_coor().get_y() <= move.get_to_coor().get_y() else move.get_to_coor().get_y()
        to_x = move.get_to_coor().get_x() if move.get_from_coor().get_x() <= move.get_to_coor().get_x() else move.get_from_coor().get_x()
        to_y = move.get_to_coor().get_y() if move.get_from_coor().get_y() <= move.get_to_coor().get_y() else move.get_from_coor().get_y()
        absolute = move.get_absolute_value()
        if absolute[0] == 0:
            for y in range(from_y + 1, to_y, 1):
                if move.board.board[from_x][y].get_chessman() != None:
                    return False
        else:
            for x in range(from_x + 1, to_x, 1):
                if move.board.board[x][from_y].get_chessman() != None:
                    return False

        return True