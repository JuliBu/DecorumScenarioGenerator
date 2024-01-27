import itertools
from copy import deepcopy
from typing import Optional, List, Union

from common.constants import AVAILABLE_ROOMS, OBJ_COLORS, POSITIONS, STYLES
from house.objects import DecorumObject
from common.utils import check_for_empty_list


class Room:
    def __init__(self, name: str, wall_color: Optional[str] = "red",
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

    def set_wall_color(self, new_color: str):
        assert new_color in OBJ_COLORS
        self.wall_color = new_color

    def get_type_from_pos(self, pos: str) -> str:
        # Stay with if - elif format as dicts are way slower
        if self.name == "bedroom1":
            if pos == "left":
                return "curiosity"
            elif pos == "middle":
                return "painting"
            elif pos == "right":
                return "lamp"
        elif self.name == "bedroom2":
            if pos == "left":
                return "painting"
            elif pos == "middle":
                return "lamp"
            elif pos == "right":
                return "curiosity"
        elif self.name == "livingroom":
            if pos == "left":
                return "curiosity"
            elif pos == "middle":
                return "lamp"
            elif pos == "right":
                return "painting"
        elif self.name == "kitchen":
            if pos == "left":
                return "lamp"
            elif pos == "middle":
                return "painting"
            elif pos == "right":
                return "curiosity"
        raise ValueError(f"Could not get type for {self.name=}, {pos=}.")

    def get_position_of_object(self, d_object: DecorumObject) -> str:
        d_obj_type = d_object.obj_type
        if self.name == "bedroom1":
            if d_obj_type == "curiosity":
                return "left"
            elif d_obj_type == "painting":
                return "middle"
            elif d_obj_type == "lamp":
                return "right"
        elif self.name == "bedroom2":
            if d_obj_type == "painting":
                return "left"
            elif d_obj_type == "lamp":
                return "middle"
            elif d_obj_type == "curiosity":
                return "right"
        elif self.name == "livingroom":
            if d_obj_type == "curiosity":
                return "left"
            elif d_obj_type == "lamp":
                return "middle"
            elif d_obj_type == "painting":
                return "right"
        elif self.name == "kitchen":
            if d_obj_type == "lamp":
                return "left"
            elif d_obj_type == "painting":
                return "middle"
            elif d_obj_type == "curiosity":
                return "right"
        raise ValueError(f"Could not get position for {self.name=}, {d_obj_type=}.")

    def place_object(self, decorum_object: DecorumObject):
        room_pos = self.get_position_of_object(decorum_object)
        if room_pos is None:
            return
        elif room_pos == "left":
            self.left_object = decorum_object
        elif room_pos == "middle":
            self.middle_object = decorum_object
        elif room_pos == "right":
            self.right_object = decorum_object
        else:
            raise ValueError("Room position is neither left nor middle nor right.")

    def remove_object_from_pos(self, pos: str):
        assert pos in POSITIONS
        if pos == "left":
            self.left_object = None
        elif pos == "middle":
            self.middle_object = None
        elif pos == "right":
            self.right_object = None

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

    def get_nr_color_elements(self, color: str) -> int:
        assert color in OBJ_COLORS
        counter = 0
        for d_object in [self.left_object, self.middle_object, self.right_object]:
            if d_object is not None and d_object.color == color:
                counter += 1
        return counter + 1 if self.wall_color == color else counter

    def get_nr_style_elements(self, style: str) -> int:
        assert style in STYLES
        counter = 0
        for d_object in [self.left_object, self.middle_object, self.right_object]:
            if d_object is not None and d_object.style == style:
                counter += 1
        return counter

    # Functions to modify room_combinations


    def __str__(self):
        player_str = ', '.join(str(player) for player in self.players)
        return f"{self.name} (Wall Color: {self.wall_color})," \
               f"Objects: {str(self.left_object)=}, {str(self.middle_object)=}, {str(self.right_object)=}, Players: {player_str}"