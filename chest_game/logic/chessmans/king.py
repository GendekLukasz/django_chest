from chest_game.logic.chessman import Chessman

class King(Chessman):
    def weight(self):
        return 1
        
    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[0,4], ],
            'white' : [[7,4], ],
        }
        
    def check_move(self, move):
        return True

    def check_move_collision(self, move):
        return True