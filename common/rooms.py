from typing import Optional, List, Union

from common.constants import AVAILABLE_ROOMS, OBJ_COLORS, POSITIONS
from common.objects import DecorumObject


class Room:
    def __init__(self, name: str, wall_color: str,
                 left_object: Optional[DecorumObject] = None,
                 middle_object: Optional[DecorumObject] = None,
                 right_object: Optional[DecorumObject] = None):
        assert name in AVAILABLE_ROOMS
        assert wall_color in OBJ_COLORS
        self.name = name
        self.wall_color = wall_color
        self.left_object = left_object
        self.middle_object = middle_object
        self.right_object = right_object
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

    def place_object(self, decorum_object: DecorumObject):
        room_pos = self.get_position_of_object(decorum_object)
        if room_pos == "left":
            self.left_object = decorum_object
        elif room_pos == "middle":
            self.middle_object = decorum_object
        elif room_pos == "right":
            self.right_object = decorum_object
        else:
            raise ValueError("Room position is neither left nor midlle nor right.")

    def get_object_from_pos(self, position: str) -> Union[DecorumObject, None]:
        assert position in POSITIONS
        if position == "left":
            return self.left_object
        elif position == "middle":
            return self.middle_object
        elif position == "right":
            return self.right_object
        else:
            return None

    def get_all_obj_by_color(self, color: str) -> List[DecorumObject]:
        output_objects = []
        for pos in POSITIONS:
            cur_obj = self.get_object_from_pos(pos)
            if cur_obj is not None:
                if cur_obj.color == color:
                    output_objects.append(cur_obj)
        return output_objects


    def add_player(self, player):
        assert len(self.players) < 2
        self.players.append(player)

    def __str__(self):
        player_str = ', '.join(str(player) for player in self.players)
        return f"{self.name} (Wall Color: {self.wall_color})," \
               f"Objects: {self.left_object=}, {self.middle_object=}, {self.right_object=}, Players: {player_str}"
