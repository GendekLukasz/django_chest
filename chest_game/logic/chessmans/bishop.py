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

    def check_move(self, from_field , to_field):
        absolute_value = from_field.get_absolute_value(to_field)
        if abs(absolute_value[0]) ==  abs(absolute_value[1]):
            return True
        else :
            return False
