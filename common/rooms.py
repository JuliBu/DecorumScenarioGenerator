from common.objects import DecorumObject


class Room:
    def __init__(self, name: str, wall_color: str):
        assert name in ["Bedroom1", "Bedroom2", "LivingRoom", "Kitchen"]
        assert wall_color in ["red", "green", "yellow", "blue"]
        self.name = name
        self.wall_color = wall_color
        self.left_object = None
        self.middle_object = None
        self.right_object = None
        self.players = []

    def get_position_of_object(self, d_object: DecorumObject) -> str:
        d_obj_type = d_object.obj_type
        if self.name == "Bedroom1":
            if d_obj_type == "Curiosity":
                return "left"
            elif d_obj_type == "Painting":
                return "middle"
            elif d_obj_type == "Lamp":
                return "right"
        elif self.name == "Bedroom2":
            if d_obj_type == "Painting":
                return "left"
            elif self.name == "Lamp":
                return "middle"
            elif self.name == "Curiosity":
                return  "right"
        elif self.name == "LivingRoom":
            if d_obj_type == "Curiosity":
                return "left"
            elif d_obj_type == "Lamp":
                return "middle"
            elif d_obj_type == "Painting":
                return "right"
        elif self.name == "Kitchen":
            if d_obj_type == "Lamp":
                return "left"
            elif d_obj_type == "Painting":
                return "middle"
            elif d_obj_type == "Curiosity":
                return "right"
        raise ValueError(f"Could not get position for {self.name=}, {d_obj_type=}.")

    def add_object(self, decorum_object: DecorumObject):
        if decorum_object.obj_type in self.object_order:
            raise ValueError(f"{decorum_object.obj_type} ist bereits im Raum vorhanden")

        self.objects.append(decorum_object)
        self.object_order.append(decorum_object.obj_type)

    def check_order(self, expected_order):
        current_order = [obj.obj_type for obj in self.objects]
        return current_order == expected_order

    def add_player(self, player):
        if len(self.players) < 2:
            self.players.append(player)
        else:
            raise ValueError(f"{self.name} can only have 2 players")

    def __str__(self):
        object_str = ', '.join(str(obj) for obj in self.objects)
        player_str = ', '.join(str(player) for player in self.players)
        return f"{self.name} (Wall Color: {self.wall_color}) - Objects: {object_str} - Players: {player_str}"
