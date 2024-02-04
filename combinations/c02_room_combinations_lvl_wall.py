import inspect
import itertools
import random

from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
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
        return f"wall_color_cond: {self.room_name=}, {nr_items=}, {mode=}"

    # ToDo: ggf Funktion wie Wenn antikes Objekt in diesem Raum enthalten, darf die Wandfarbe nicht blau sein

    def get_random_method(self):
        weighted_choices = [1, 1, 2, 2, 0, 3]
        params = {
            'nr_items': random.choice(weighted_choices),
            'color': random.choice(OBJ_COLORS),
            'mode': random.choice(["min", "max"]),
            'style': random.choice(STYLES),
            'obj_type': random.choice(OBJ_TYPES),
            'should_be_available': random.choice([True, False])
        }
        methods = [
            self.filter_color_and_quantity_wall,
        ]
        random_method = random.choice(methods)
        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)