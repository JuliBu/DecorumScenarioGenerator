class Room:
    def __init__(self, name, wall_color):
        self.name = name
        self.wall_color = wall_color
        self.objects = []
        self.object_order = []

    def add_object(self, decorum_object):
        # Überprüfen, ob der Objekttyp bereits im Raum vorhanden ist
        if decorum_object.obj_type in self.object_order:
            raise ValueError(f"{decorum_object.obj_type} ist bereits im Raum vorhanden")

        self.objects.append(decorum_object)
        self.object_order.append(decorum_object.obj_type)

    def check_order(self, expected_order):
        current_order = [obj.obj_type for obj in self.objects]
        return current_order == expected_order

    def __str__(self):
        object_str = ', '.join(str(obj) for obj in self.objects)
        return f"{self.name} (Wandfarbe: {self.wall_color}) - Objekte: {object_str}"
