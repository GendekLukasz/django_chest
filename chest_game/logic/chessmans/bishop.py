from chest_game.logic.chessman import Chessman

class Bishop(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[0,2], [0,5]],
            'white' : [[7,2], [7,5]],
        }

    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if abs(absolute_value[0]) ==  abs(absolute_value[1]):
            return True
        else :
            return False

    def check_move_collision(self, move):
        return True
        