import itertools

from common.constants import OBJ_COLORS, POSITIONS, STYLES, OBJ_TYPES
from common.utils import check_for_empty_list
from house.objects import get_obj_style
from house.rooms.rooms import get_type_from_room_and_pos


# class Combinations:
#     def __init__(self, room_name: str):
#         wall_colors = OBJ_COLORS
#         self.object_combinations = list(itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS)))
#         self.bedroom1_combinations = list(itertools.product(self.object_combinations, wall_colors))
#         self.bedroom2_combinations = list(itertools.product(self.object_combinations, wall_colors))


class BedroomItemCombinations:
    def __init__(self, bedroom_name: str):
        self.object_combinations = list(itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS)))
        self.bedroom_name = bedroom_name

    def filter_items_by_color_and_quantity(self, nr_items: int, color: str, mode: str):
        assert 0 <= nr_items <= 3
        assert color in OBJ_COLORS
        assert mode in ["min", "max"]

        new_combs = []
        for obj_comb in self.object_combinations:
            if mode == "min" and obj_comb.count(color) >= nr_items:
                new_combs.append(obj_comb)
            elif mode == "max" and obj_comb.count(color) <= nr_items:
                new_combs.append(obj_comb)

        check_for_empty_list(new_combs)
        self.object_combinations = new_combs

    def filter_items_by_style_and_quantity(self, nr_items: int, style: str, mode: str):
        assert 0 <= nr_items <= 3
        assert style in STYLES
        assert mode in ["min", "max"]

        new_combs = []
        for obj_comb in self.object_combinations:
            # left_color, middle_color, right_color = obj_comb
            # left_type, middle_type, right_type = [get_type_from_room_and_pos(self.bedroom_name, pos) for pos in ["left", "middle", "right"]]
            # left_style, middle_style, right_style = [get_obj_style(color, obj_type) for color, obj_type in zip([left_color, middle_color, right_color], [left_type, middle_type, right_type])]
            # styles = [left_style, middle_style, right_style]

            styles = [get_obj_style(color, get_type_from_room_and_pos(self.bedroom_name, pos)) for color, pos in
                      zip(obj_comb, ["left", "middle", "right"])]

            if mode == "min" and styles.count(style) >= nr_items:
                new_combs.append(obj_comb)
            elif mode == "max" and styles.count(style) <= nr_items:
                new_combs.append(obj_comb)

        check_for_empty_list(new_combs)
        self.object_combinations = new_combs

    def filter_availability_of_type(self, type: str, should_be_available: bool):
        assert type in OBJ_TYPES
        new_combs = []
        for obj_comb in self.object_combinations:
            left_color, middle_color, right_color = obj_comb
            left_type, middle_type, right_type = [get_type_from_room_and_pos(self.bedroom_name, pos) for pos in ["left", "middle", "right"]]
            for obj_type, obj_color in zip([left_type, middle_type, right_type],
                                           [left_color, middle_color, right_color]):
                if obj_type == type and (obj_color is not None) == should_be_available:
                    new_combs.append(obj_comb)
        check_for_empty_list(new_combs)
        self.object_combinations = new_combs


class BedroomCombinationsWithWalls:
    def __init__(self, item_combinations):
        wall_colors = OBJ_COLORS
        self.bedroom_combinations = list(itertools.product(item_combinations, wall_colors))


class UpperFloorCombinationsOnlyRooms:
    def __init__(self, bedroom1_combinations, bedroom2_combinations):
        self.upper_floor_combinations_only_rooms = list(itertools.product(bedroom1_combinations, bedroom2_combinations))


class UpperFloorCombinationsWithPlayers:
    def __init__(self, upper_floor_combinations_only_rooms):
        player_combs = [
            [{1, 2}, {3, 4}],
            [{1, 3}, {2, 4}],
            [{1, 4}, {2, 3}],
            [{2, 3}, {1, 4}],
            [{2, 4}, {1, 3}],
            [{3, 4}, {1, 2}]
            ]
        self.upper_floor_combinations_with_players = list(itertools.product(upper_floor_combinations_only_rooms, player_combs))





