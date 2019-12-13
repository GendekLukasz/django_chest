class Coordinates():

    axis_x = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7}

    axis_y = {
        '1' : 7,
        '2' : 6,
        '3' : 5,
        '4' : 4,
        '5' : 3,
        '6' : 2,
        '7' : 1,
        '8' : 0}

    def __init__(self, field_name):
        self.field_name = field_name
        self.coordinates = self.field_name_to_coordinates(field_name)

    def field_name_to_coordinates(self, field_name):
        if len(field_name) == 2:
            y = Coordinates.axis_y[field_name[1]]
            x = Coordinates.axis_x[field_name[0]]
            return [x,y]
        else:
            return None

    def get_field_name(self):
        return self.field_name

    def get_coordinates(self):
        return self.coordinates

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def get_absolute_value(self, coordinates):
        return [coordinates.get_x() - self.get_x(),coordinates.get_y() - self.get_y()]

    def compare_coordinates(self, coordinates):
        return self.get_x() == coordinates.get_x() and self.get_y() == coordinates.get_y()