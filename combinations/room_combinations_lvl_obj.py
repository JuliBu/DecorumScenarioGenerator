import itertools
from copy import deepcopy

from common.constants import OBJ_COLORS, POSITIONS
from common.utils import check_for_empty_list


class Combinations:
    def __init__(self, room_name: str):
        wall_colors = OBJ_COLORS
        self.object_combinations = list(itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS)))
        self.bedroom1_combinations = list(itertools.product(self.object_combinations, wall_colors))
        self.bedroom2_combinations = list(itertools.product(self.object_combinations, wall_colors))

    def add_player_complexity(self):
        self.upper_floor_combinations_with_players = list(itertools.product(self.bedroom1_combinations, self.bedroom2_combinations))


    def filter_by_
    def filter_items_by_color_and_quantity(self, nr_items: int, color: str, mode: str):
        assert 0 < nr_items < 4
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





