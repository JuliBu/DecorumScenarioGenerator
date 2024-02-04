import itertools

from common.constants import OBJ_COLORS
from common.utils import check_for_empty_list


class RoomCombinationsWithWalls:
    def __init__(self, room_name: str, item_combinations):
        wall_colors = OBJ_COLORS
        self.room_name = room_name
        self.room_wall_combinations = list(itertools.product(item_combinations, wall_colors))

    def __len__(self):
        return len(self.room_wall_combinations)

    def filter_color_and_quantity_wall(self, nr_items: int, mode: str):
        assert 0 <= nr_items <= 3
        assert mode in ["min", "max"]

        new_combs = []
        for obj_comb, wall_color in self.room_wall_combinations:
            if mode == "min" and obj_comb.count(wall_color) >= nr_items:
                new_combs.append((obj_comb, wall_color))
            elif mode == "max" and obj_comb.count(wall_color) <= nr_items:
                new_combs.append((obj_comb, wall_color))

        check_for_empty_list(new_combs)
        self.room_wall_combinations = new_combs
        return f"{self.room_name=}, {nr_items=}, {mode=}"

    # ToDo: ggf Funktion wie Wenn antikes Objekt in diesem Raum enthalten, darf die Wandfarbe nicht blau sein
