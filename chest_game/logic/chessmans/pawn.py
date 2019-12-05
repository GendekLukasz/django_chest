from chest_game.logic.chessman import Chessman

class Pawn(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7]],
            'white' : [[6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7]],
        }
   
    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if move.get_chessman_to_move().get_colour() == 'Black': 
            if move.check_its_attack_on_opponent():
                if  (absolute_value[1] == 1 or absolute_value[1] == -1) and absolute_value[0] == -1:
                    return True
            else:
                if self.get_number_of_moves() == 0 and absolute_value[1] == 0 and (absolute_value[0] == -1 or absolute_value[0] == -2):
                    return True
                elif absolute_value[1] == 0 and absolute_value[0] == -1: 
                    return True
        else:
            if move.check_its_attack_on_opponent():
                if  (absolute_value[0] == 1 or absolute_value[0] == -1) and absolute_value[1] == 1:
                    return True
            else:
                if self.get_number_of_moves() == 0 and absolute_value[1] == 0 and (absolute_value[0] == 1 or absolute_value[0] == 2):
                    return True
                elif absolute_value[1] == 0 and absolute_value[0] == 1: 
                    return True
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

        return True