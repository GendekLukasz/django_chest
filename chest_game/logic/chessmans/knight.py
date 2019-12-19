from chest_game.logic.chessman import Chessman

class Knight(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['b8', 'g8'],
            'white' : ['b1', 'g1'],
        }
        
    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if abs(absolute_value[0]) == 1 and abs(absolute_value[1]) == 2 or abs(absolute_value[0]) == 2 and abs(absolute_value[1]) == 1:
            return True
        else :
            return False

    def check_move_collision(self, move):
        return True

    def get_list_of_coordinates_to_check_before_mate(self, move):
        return None