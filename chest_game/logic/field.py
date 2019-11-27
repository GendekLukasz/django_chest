class Field():
    def __init__(self, colour):
        self.__colour = colour
        self.chessman = None
        
    def get_colour(self):
        return self.__colour

    def set_chessman(self, chessman):
        self.chessman = chessman
    
    def get_chessman(self):
        return self.chessman

    def delete_chessman(self):
        old_chessman = self.chessman
        self.chessman = None
        return old_chessman