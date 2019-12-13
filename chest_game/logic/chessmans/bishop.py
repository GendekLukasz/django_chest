from chest_game.logic.chessman import Chessman

class Bishop(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['c8', 'f8'],
            'white' : ['c1', 'f1'],
        }

    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if abs(absolute_value[0]) ==  abs(absolute_value[1]):
            return True
        else :
            return False

    def check_move_collision(self, move):
        from_x = move.get_from_coor().get_x()
        from_y = move.get_from_coor().get_y()
        to_x = move.get_to_coor().get_x()
        to_y = move.get_to_coor().get_y()
        absolute_value = move.get_absolute_value()
        x_difference = 1
        if absolute_value[0] < 0:
            x_difference = -1
        y_difference = 1
        if absolute_value[1] < 0:
            y_difference = -1
        for y in range(from_y + y_difference, to_y, y_difference):
            for x in range(from_x + x_difference, to_x, x_difference):
                if abs(x - from_x) == abs(y - from_y):
                    if move.board.board[y][x].get_chessman() != None:
                        return False
        return True