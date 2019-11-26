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