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

    def check_move(self, from_field , to_field):
        absolute_value = from_field.get_absolute_value(to_field)
        if absolute_value[0] == 0 or absolute_value[1] == 0:
            return True
        else :
            return False