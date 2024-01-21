import itertools

from tqdm import tqdm

from common.constants import OBJ_COLORS, POSITIONS
from common.objects import DecorumObject, get_obj_style
from common.player import Player
from common.rooms import Room
from sys import getsizeof


class House:
    def __init__(self, bedroom1: Room, bedroom2: Room, living_room: Room, kitchen: Room):
        self.bedroom1 = bedroom1
        self.bedroom2 = bedroom2
        self.living_room = living_room
        self.kitchen = kitchen
        self.all_rooms = [bedroom1, bedroom2, living_room, kitchen]

    def check_example_condition(self):
        if (self.bedroom2.get_nr_color_elements("blue") > 2) \
                and (self.kitchen.get_nr_color_elements("green") < 2) \
                and (self.bedroom1.get_nr_style_elements("antique") > 3):
            return True

    def old_iter_modifications(self):
        mod_counter = 0
        for room in self.all_rooms:
            for room_color in OBJ_COLORS:
                # for pos in POSITIONS:
                #     obj_type = room.get_type_from_pos(pos)
                #     for obj_color in OBJ_COLORS:
                for objects in itertools.product(OBJ_COLORS, repeat=len(POSITIONS)):
                    for pos, obj_color in zip(POSITIONS, objects):
                        obj_type = room.get_type_from_pos(pos)
                        if obj_color is None:
                            room.remove_object_from_pos(pos)
                        else:
                            obj_style = get_obj_style(obj_color, obj_type)
                            deco_obj = DecorumObject(obj_type, obj_color, obj_style)
                            room.place_object(deco_obj)
                        room.set_wall_color(room_color)
                        mod_counter += 1
                        print(self)
                        print(f"\n{mod_counter=}\n")
                        obj_style = get_obj_style(obj_color, obj_type)
                        deco_obj = DecorumObject(obj_type, obj_color, obj_style)
                        room.place_object(deco_obj)
                        if self.check_example_condition():
                            print("Solution found:")
                            print(self)






        all_combinations = list(itertools.product(wall_combinations, room_combinations))
        print(len(all_combinations))
        # mod_counter = 0
        # for room in self.all_rooms:
        #     for room_color in OBJ_COLORS:
        #         # for pos in POSITIONS:
        #         #     obj_type = room.get_type_from_pos(pos)
        #         #     for obj_color in OBJ_COLORS:
        #         for objects in itertools.product(OBJ_COLORS, repeat=len(POSITIONS)):
        #             for pos, obj_color in zip(POSITIONS, objects):
        #                 obj_type = room.get_type_from_pos(pos)
        #                 if obj_color is None:
        #                     room.remove_object_from_pos(pos)
        #                 else:
        #                     obj_style = get_obj_style(obj_color, obj_type)
        #                     deco_obj = DecorumObject(obj_type, obj_color, obj_style)
        #                     room.place_object(deco_obj)
        #                 room.set_wall_color(room_color)
        #                 mod_counter += 1
        #                 print(self)
        #                 print(f"\n{mod_counter=}\n")
        #                 obj_style = get_obj_style(obj_color, obj_type)
        #                 deco_obj = DecorumObject(obj_type, obj_color, obj_style)
        #                 room.place_object(deco_obj)
        #                 if self.check_example_condition():
        #                     print("Solution found:")
        #                     print(self)

    def __str__(self):
        return f"House Structure:\n{self.bedroom1}\n{self.bedroom2}\n{self.living_room}\n{self.kitchen}"

