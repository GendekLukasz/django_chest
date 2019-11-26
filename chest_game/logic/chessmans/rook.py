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