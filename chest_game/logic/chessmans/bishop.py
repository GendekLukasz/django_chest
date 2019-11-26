from chest_game.logic.chessman import Chessman

class Bishop(Chessman):
    def weight(self):
        return 1

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : [[0,2], [0,5]],
            'white' : [[7,2], [7,5]],
        }