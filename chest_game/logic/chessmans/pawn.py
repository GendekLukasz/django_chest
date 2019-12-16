from chest_game.logic.chessman import Chessman

class Pawn(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            'white' : ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
        }
   
    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if move.get_chessman_to_move().get_colour() == 'Black': 
            if move.check_its_attack_on_opponent():
                if  (absolute_value[0] == -1 or absolute_value[0] == 1) and absolute_value[1] == 1:
                    return True
            else:
                if self.get_number_of_moves() == 0 and absolute_value[0] == 0 and (absolute_value[1] == 1 or absolute_value[1] == 2):
                    return True
                elif absolute_value[0] == 0 and absolute_value[1] == 1: 
                    return True
        else:
            if move.check_its_attack_on_opponent():
                if  (absolute_value[1] == -1 or absolute_value[1] == 1) and absolute_value[0] == -1:
                    return True
            else:
                if self.get_number_of_moves() == 0 and absolute_value[0] == 0 and (absolute_value[1] == -1 or absolute_value[1] == -2):
                    return True
                elif absolute_value[0] == 0 and absolute_value[1] == -1: 
                    return True
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
                if move.board.board[y][from_x].get_chessman() != None:
                    return False
        return True

    def get_list_of_coordinates_to_check_before_mate(self, move):
        return None