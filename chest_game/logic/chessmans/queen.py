from chest_game.logic.chessman import Chessman

class Queen(Chessman):
    def weight(self):
        return 1
        
    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['d8'],
            'white' : ['d1'],
        }
        
    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if absolute_value[0] == 0 or absolute_value[1] == 0:
            return True
        elif abs(absolute_value[0]) ==  abs(absolute_value[1]):
            return True
        else:
            return False

    def check_move_collision(self, move):
        from_x = self.get_coordinates_for_coolision_check(move)['from_x']
        from_y = self.get_coordinates_for_coolision_check(move)['from_y']
        to_x = self.get_coordinates_for_coolision_check(move)['to_x']
        to_y = self.get_coordinates_for_coolision_check(move)['to_y']
        absolute = move.get_absolute_value()
        if absolute[0] == 0:
            for y in range(from_y + 1, to_y, 1):
                if move.board.board[from_x][y].get_chessman() != None:
                    return False
        elif absolute[1] == 0:
            for x in range(from_x + 1, to_x, 1):
                if move.board.board[x][from_y].get_chessman() != None:
                    return False
        else:
            for y in range(from_y + 1, to_y, 1):
                for x in range(from_x + 1, to_x, 1):
                    if x - from_x == y - from_y:
                        if move.board.board[x][y].get_chessman() != None:
                            return False
        return True