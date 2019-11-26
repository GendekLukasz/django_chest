class Field():
    def __init__(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def set_chessman(self, chessman):
        self.chessman = chessman
    
    def delete_chessman(self):
        old_chessman = self.chessman
        self.chessman = None
        return old_chessman