from chest_game.logic.chessman import Chessman

class King(Chessman):


    def weight(self):
        return 1

    def set_castling(self):
        self.castling = True

    def get_castling(self):
        if not hasattr(self, 'castling'):
            self.castling = False
        return self.castling

    def castling_done(self):
        self.castling = False    

    @staticmethod
    def get_starting_points_list():
        return {
            'black' : ['e8'],
            'white' : ['e1'],
        }
        
    def check_move(self, move):
        absolute_value = move.get_absolute_value()
        if absolute_value[1] == 0 and abs(absolute_value[0]) == 2:
            self.set_castling()
            return True
        elif abs(absolute_value[0]) == 1 and abs(absolute_value[1]) == 1 or abs(absolute_value[0]) == 1 and abs(absolute_value[1]) == 0 or abs(absolute_value[0]) == 0 and abs(absolute_value[1]) == 1:
            return True
        else:
            return False

    def check_move_collision(self, move):
        return True

    def get_list_of_coordinates_to_check_before_mate(self, move):
        return None