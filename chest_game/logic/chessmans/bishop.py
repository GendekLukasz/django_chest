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
        for y in range(from_y + 1, to_y, 1):
            for x in range(from_x + 1, to_x, 1):

                if x - from_x == y - from_y:
                                    
                    print(x)
                    print(y)
                    if move.board.board[x][y].get_chessman() != None:

                        return False
        return True