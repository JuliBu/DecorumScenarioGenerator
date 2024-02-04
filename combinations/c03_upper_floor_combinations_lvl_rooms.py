import inspect
import itertools
import random

from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
from common.utils import check_for_inval_cond


class UpperFloorCombinationsOnlyRooms:
    def __init__(self, bedroom1_combinations, bedroom2_combinations):
        self.upper_floor_combinations_only_rooms = list(itertools.product(bedroom1_combinations, bedroom2_combinations))

    def __len__(self):
        return len(self.upper_floor_combinations_only_rooms)

    def filter_floor_items_by_color_and_quantity(self, nr_items: int, color: str, mode: str):
        assert 0 <= nr_items <= 6
        assert color in OBJ_COLORS
        assert mode in ["min", "max"]

        new_combs = []
        for upper_floor in self.upper_floor_combinations_only_rooms:
            left_room, right_room = upper_floor
            color_counter = (left_room[0] + right_room[0]).count(color)
            if mode == "min" and color_counter >= nr_items:
                new_combs.append(upper_floor)
            elif mode == "max" and color_counter <= nr_items:
                new_combs.append(upper_floor)
        check_for_inval_cond(new_combs, len(self.upper_floor_combinations_only_rooms))
        self.upper_floor_combinations_only_rooms = new_combs
        return f"Upper floor, {nr_items=}, {color=}, {mode=}"

    def get_random_method(self):
        weighted_choices = [
            0,
            1, 1,
            2, 2, 2,
            3, 3, 3,
            4, 4,
            5, 5,
            6
            ]
        params = {
            'nr_items': random.choice(weighted_choices),
            'color': random.choice(OBJ_COLORS),
            'mode': random.choice(["min", "max"]),
            'style': random.choice(STYLES),
            'obj_type': random.choice(OBJ_TYPES),
            'should_be_available': random.choice([True, False])
        }
        methods = [
            self.filter_floor_items_by_color_and_quantity,
        ]
        random_method = random.choice(methods)
        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)