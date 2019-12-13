from chest_game.logic.chessman import Chessman

class Rook(Chessman):
    def weight(self):
        return 1
        
    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['a8', 'h8'],
            'white' : ['a1', 'h1'],
        }

    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if absolute_value[0] == 0 or absolute_value[1] == 0:
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
        if absolute_value[0] == 0:
            for y in range(from_y + y_difference, to_y, y_difference):
                if move.board.board[y][from_x].get_chessman() != None:
                    return False
        elif absolute_value[1] == 0:
            for x in range(from_x + x_difference, to_x, x_difference):
                if move.board.board[from_y][x].get_chessman() != None:
                    return False

        return True