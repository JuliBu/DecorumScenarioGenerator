from typing import Union

from common.constants import ALLOWED_COMBINATIONS, OBJ_COLORS, OBJ_TYPES


def get_obj_style(obj_color: str, obj_type: str) -> Union[str, None]:
    # assert obj_type in OBJ_TYPES
    if obj_color is None:
        return None
    assert obj_color in OBJ_COLORS
    if obj_type == "painting":
        if obj_color == "red":
            return "modern"
        elif obj_color == "green":
            return "antique"
        elif obj_color == "blue":
            return "retro"
        elif obj_color == "yellow":
            return "rare"
    elif obj_type == "curiosity":
        if obj_color == "red":
            return "rare"
        elif obj_color == "green":
            return "modern"
        elif obj_color == "blue":
            return "antique"
        elif obj_color == "yellow":
            return "retro"
    elif obj_type == "lamp":
        if obj_color == "red":
            return "retro"
        elif obj_color == "green":
            return "rare"
        elif obj_color == "blue":
            return "modern"
        elif obj_color == "yellow":
            return "antique"
    raise ValueError(f"Could not get obj style for {obj_type=}, {obj_color=}")

class DecorumObject:
    def __init__(self, obj_type, color, style):
        self.obj_type = obj_type
        self.color = color
        self.style = style
        if (self.obj_type, self.color, self.style) not in ALLOWED_COMBINATIONS:
            raise ValueError("Invalid Combination of DecorumObject")

    def __str__(self):
        return f"{self.color} {self.style} {self.obj_type}"
