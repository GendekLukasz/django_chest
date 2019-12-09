from chest_game.logic.chessman import Chessman

class King(Chessman):
    def weight(self):
        return 1
        
    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['e8'],
            'white' : ['e1'],
        }
        
    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if abs(absolute_value[0]) == 1 and abs(absolute_value[1]) == 1 or abs(absolute_value[0]) == 1 and abs(absolute_value[1]) == 0 or abs(absolute_value[0]) == 0 and abs(absolute_value[1]) == 1:
            return True
        else :
            return False

    def check_move_collision(self, move):
        return True