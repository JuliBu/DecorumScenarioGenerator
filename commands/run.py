from common.constants import AVAILABLE_ROOMS, POSITIONS, OBJ_COLORS, OBJ_TYPES
from common.objects import get_obj_style, DecorumObject
from common.rooms import Room



for room_name in AVAILABLE_ROOMS:
    for room_color in OBJ_COLORS:
        room = Room(room_name, room_color)
        for pos in POSITIONS:
            obj_type = room.get_type_from_pos(pos)
            for obj_color in OBJ_COLORS:
                obj_style = get_obj_style(obj_color, obj_type)
                deco_obj = DecorumObject(obj_type, obj_color, obj_style)
                room.place_object(deco_obj)

