from chest_game.logic.chessman import Chessman

class Pawn(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7]],
            'white' : [[6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7]],
        }
