
from chest_game.logic.coordinates import Coordinates
class ChessmanList():
    def __init__(self):
        self.list_of_chessmans = {
            'Black' : [],
            'White' : []
        }

    def add_black_chess(self, chessman):
        self.list_of_chessmans['Black'].append(chessman)

    def add_white_chess(self, chessman):
        self.list_of_chessmans['White'].append(chessman)

    def get_black_king(self):
        for piece in self.list_of_chessmans['Black']:
            if piece.__class__.__name__ == 'King':
                return piece

        return None

    def get_white_king(self):
        for piece in self.list_of_chessmans['White']:
            if piece.__class__.__name__ == 'King':
                return piece

        return None

    def get_all_black_chessmans(self):
        return self.list_of_chessmans['Black']

    def get_all_white_chessmans(self):
        return self.list_of_chessmans['White']

    def get_chessman_by_coordinates(self, coordinates):
        for piece in self.list_of_chessmans['Black']:
            if piece.coordinates.compare_coordinates(coordinates):
                return piece
                
        for piece in self.list_of_chessmans['White']:
            if piece.coordinates.compare_coordinates(coordinates):
                return piece

        return None

    def update_coordinates_by_move(self, move):
        self.get_chessman_by_coordinates(move.get_from_coor()).set_coordinates(move.get_to_coor())
    
    def delete_chessman_from_list(self, coordinates):
        chessman_to_delete = self.get_chessman_by_coordinates(coordinates)
        if chessman_to_delete != None:
            colour = chessman_to_delete.get_colour()
            if colour == 'Black':
                self.list_of_chessmans['Black'].remove(chessman_to_delete)
            else:
                self.list_of_chessmans['White'].remove(chessman_to_delete)
