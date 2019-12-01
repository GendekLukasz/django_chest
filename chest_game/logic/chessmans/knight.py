from chest_game.logic.chessman import Chessman

class Knight(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[0,1], [0,6]],
            'white' : [[7,1], [7,6]],
        }
        
    def check_move(self, from_field , to_field):
        absolute_value = from_field.get_absolute_value(to_field)
        if abs(absolute_value[0]) == 1 and abs(absolute_value[1]) == 2 or abs(absolute_value[0]) == 2 and abs(absolute_value[1]) == 1:
            return True
        else :
            return False