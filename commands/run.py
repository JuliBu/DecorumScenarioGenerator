import itertools
from sys import getsizeof

from tqdm import tqdm

from common.constants import AVAILABLE_ROOMS, POSITIONS, OBJ_COLORS, OBJ_TYPES
from common.house import House
from common.objects import get_obj_style, DecorumObject
from common.rooms import Room


init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")

# house = House(init_bedroom1, init_bedroom2, init_livingroom, init_kitchen)
# house.iter_modifications()

def create_and_place_objects(room, color_combination):
    for pos, color in zip(['left', 'middle', 'right'], color_combination):
        obj_type = room.get_type_from_pos(pos)
        obj_style = get_obj_style(color, obj_type)
        if obj_style is not None:
            room.place_object(DecorumObject(obj_type, color, obj_style))

def iter_modifications():
    wall_colors = OBJ_COLORS
    wall_combinations = itertools.product(wall_colors, repeat=len(AVAILABLE_ROOMS))
    object_combinations = itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS))
    room_combinations = itertools.product(object_combinations, repeat=len(AVAILABLE_ROOMS))

    for wall_combination in wall_combinations:
        for room_combination in tqdm(room_combinations):
            house = House(
                Room('bedroom1', wall_combination[0]),
                Room('bedroom2', wall_combination[1]),
                Room('livingroom', wall_combination[2]),
                Room('kitchen', wall_combination[3])
            )

            for room, color_combination in zip(house.all_rooms, room_combination):
                create_and_place_objects(room, color_combination)

            house.check_example_condition()

# def iter_modifications():
#     wall_colors = OBJ_COLORS
#     wall_combinations = list(itertools.product(wall_colors, repeat=len(AVAILABLE_ROOMS)))
#     object_combinations = list(itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS)))
#     room_combinations = list(itertools.product(object_combinations, repeat=len(AVAILABLE_ROOMS)))
#     print(getsizeof(room_combinations))
#     for wall_combination in wall_combinations:
#         for room_combination in tqdm(room_combinations):
#             bedroom1 = Room('bedroom1', wall_combination[0])
#             left_color = room_combination[0][0]
#             left_type = bedroom1.get_type_from_pos('left')
#             left_style = get_obj_style(left_color, left_type)
#             if left_style is not None:
#                 bedroom1.place_object(DecorumObject(left_type, left_color, left_style))
#             middle_color = room_combination[0][1]
#             middle_type = bedroom1.get_type_from_pos('middle')
#             middle_style = get_obj_style(middle_color, middle_type)
#             if middle_style is not None:
#                 bedroom1.place_object(DecorumObject(middle_type, middle_color, middle_style))
#             right_color = room_combination[0][2]
#             right_type = bedroom1.get_type_from_pos('right')
#             right_style = get_obj_style(right_color, right_type)
#             if right_style is not None:
#                 bedroom1.place_object(DecorumObject(right_type, right_color, right_style))
#
#             bedroom2 = Room('bedroom2', wall_combination[0])
#             left_color = room_combination[1][0]
#             left_type = bedroom2.get_type_from_pos('left')
#             left_style = get_obj_style(left_color, left_type)
#             if left_style is not None:
#                 bedroom2.place_object(DecorumObject(left_type, left_color, left_style))
#             middle_color = room_combination[1][1]
#             middle_type = bedroom2.get_type_from_pos('middle')
#             middle_style = get_obj_style(middle_color, middle_type)
#             if middle_style is not None:
#                 bedroom2.place_object(DecorumObject(middle_type, middle_color, middle_style))
#             right_color = room_combination[1][2]
#             right_type = bedroom2.get_type_from_pos('right')
#             right_style = get_obj_style(right_color, right_type)
#             if right_style is not None:
#                 bedroom2.place_object(DecorumObject(right_type, right_color, right_style))
#
#             livingroom = Room('livingroom', wall_combination[0])
#             left_color = room_combination[2][0]
#             left_type = livingroom.get_type_from_pos('left')
#             left_style = get_obj_style(left_color, left_type)
#             if left_style is not None:
#                 livingroom.place_object(DecorumObject(left_type, left_color, left_style))
#             middle_color = room_combination[2][1]
#             middle_type = livingroom.get_type_from_pos('middle')
#             middle_style = get_obj_style(middle_color, middle_type)
#             if middle_style is not None:
#                 livingroom.place_object(DecorumObject(middle_type, middle_color, middle_style))
#             right_color = room_combination[2][2]
#             right_type = livingroom.get_type_from_pos('right')
#             right_style = get_obj_style(right_color, right_type)
#             if right_style is not None:
#                 livingroom.place_object(DecorumObject(right_type, right_color, right_style))
#
#             kitchen = Room('kitchen', wall_combination[0])
#             left_color = room_combination[3][0]
#             left_type = kitchen.get_type_from_pos('left')
#             left_style = get_obj_style(left_color, left_type)
#             if left_style is not None:
#                 kitchen.place_object(DecorumObject(left_type, left_color, left_style))
#             middle_color = room_combination[3][1]
#             middle_type = kitchen.get_type_from_pos('middle')
#             middle_style = get_obj_style(middle_color, middle_type)
#             if middle_style is not None:
#                 kitchen.place_object(DecorumObject(middle_type, middle_color, middle_style))
#             right_color = room_combination[3][2]
#             right_type = kitchen.get_type_from_pos('right')
#             right_style = get_obj_style(right_color, right_type)
#             if right_style is not None:
#                 kitchen.place_object(DecorumObject(right_type, right_color, right_style))
#
#             house = House(bedroom1, bedroom2, livingroom, kitchen)
#             house.check_example_condition()
#             # print("Test")

if __name__ == '__main__':
    iter_modifications()
