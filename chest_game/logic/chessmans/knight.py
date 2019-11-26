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