import itertools
from copy import deepcopy
from typing import Optional, List, Union, Tuple

from common.constants import AVAILABLE_ROOMS, OBJ_COLORS, POSITIONS, STYLES
from house.objects import DecorumObject, get_obj_style
from common.utils import check_for_inval_cond


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

    def set_wall_color(self, new_color: str):
        assert new_color in OBJ_COLORS
        self.wall_color = new_color

    def place_object(self, decorum_object: DecorumObject):
        room_pos = get_position_of_object_from_room_and_type(self.name, decorum_object.obj_type)
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
        return f"{self.name} (Wall Color: {self.wall_color})," \
               f"Objects: {str(self.left_object)=}, {str(self.middle_object)=}, {str(self.right_object)=}"


def get_type_from_room_and_pos(room_name: str, pos: str) -> str:
    assert room_name in AVAILABLE_ROOMS
    assert pos in POSITIONS

    if room_name == "bedroom1":
        if pos == "left":
            return "curiosity"
        elif pos == "middle":
            return "painting"
        elif pos == "right":
            return "lamp"
    elif room_name == "bedroom2":
        if pos == "left":
            return "painting"
        elif pos == "middle":
            return "lamp"
        elif pos == "right":
            return "curiosity"
    elif room_name == "livingroom":
        if pos == "left":
            return "curiosity"
        elif pos == "middle":
            return "lamp"
        elif pos == "right":
            return "painting"
    elif room_name == "kitchen":
        if pos == "left":
            return "lamp"
        elif pos == "middle":
            return "painting"
        elif pos == "right":
            return "curiosity"
    raise ValueError(f"Could not get type for { room_name=}, {pos=}.")


def get_position_of_object_from_room_and_type(room_name: str, d_obj_type: str) -> str:
    assert room_name in AVAILABLE_ROOMS
    assert d_obj_type in STYLES

    if room_name == "bedroom1":
        if d_obj_type == "curiosity":
            return "left"
        elif d_obj_type == "painting":
            return "middle"
        elif d_obj_type == "lamp":
            return "right"
    elif room_name == "bedroom2":
        if d_obj_type == "painting":
            return "left"
        elif d_obj_type == "lamp":
            return "middle"
        elif d_obj_type == "curiosity":
            return "right"
    elif room_name == "livingroom":
        if d_obj_type == "curiosity":
            return "left"
        elif d_obj_type == "lamp":
            return "middle"
        elif d_obj_type == "painting":
            return "right"
    elif room_name == "kitchen":
        if d_obj_type == "lamp":
            return "left"
        elif d_obj_type == "painting":
            return "middle"
        elif d_obj_type == "curiosity":
            return "right"
    raise ValueError(f"Could not get position for { room_name=}, {d_obj_type=}.")

def get_room_from_color_and_name(room_name: str, color_comb: Tuple[Tuple[str, str, str], str]) -> Room:
    obj_colors, wall_color = color_comb
    left_color, middle_color, right_color = obj_colors
    left_type, middle_type, right_type = get_type_from_room_and_pos(room_name, "left"), get_type_from_room_and_pos(room_name, "middle"), get_type_from_room_and_pos(room_name, "right")
    left_style, middle_style, right_style = get_obj_style(left_color, left_type), get_obj_style(middle_color, middle_type), get_obj_style(right_color, right_type)
    left_obj = DecorumObject(left_type, left_color, left_style) if left_color is not None else None
    middle_obj = DecorumObject(middle_type, middle_color, middle_style) if middle_color is not None else None
    right_obj = DecorumObject(right_type, right_color, right_style) if right_color is not None else None
    return Room(room_name, wall_color, left_obj, middle_obj, right_obj)