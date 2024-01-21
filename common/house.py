import itertools

from common.constants import OBJ_COLORS, AVAILABLE_ROOMS
from common.rooms import Room


class House:
    def __init__(self, bedroom1: Room, bedroom2: Room, living_room: Room, kitchen: Room):
        self.bedroom1 = bedroom1
        self.bedroom2 = bedroom2
        self.living_room = living_room
        self.kitchen = kitchen
        self.all_rooms = [bedroom1, bedroom2, living_room, kitchen]
        self.wall_combinations = itertools.product(OBJ_COLORS, repeat=len(AVAILABLE_ROOMS))

    def check_example_condition(self):
        if (self.bedroom2.get_nr_color_elements("blue") > 2) \
                and (self.kitchen.get_nr_color_elements("green") < 2) \
                and (self.bedroom1.get_nr_style_elements("antique") > 3):
            return True


    def __str__(self):
        return f"House Structure:\n{self.bedroom1}\n{self.bedroom2}\n{self.living_room}\n{self.kitchen}"

