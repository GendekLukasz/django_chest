from chest_game.logic.chessman import Chessman

class Queen(Chessman):
    def weight(self):
        return 1
        
    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[0,3]],
            'white' : [[7,3]],
        }
        
    def check_move(self, move):
        return True

    def check_move_collision(self, move):
        return True