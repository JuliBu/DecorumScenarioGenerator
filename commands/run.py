from common.constants import AVAILABLE_ROOMS, POSITIONS, OBJ_COLORS, OBJ_TYPES
from common.house import House
from common.objects import get_obj_style, DecorumObject
from common.rooms import Room


init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")

house = House(init_bedroom1, init_bedroom2, init_livingroom, init_kitchen)
house.iter_modifications()

