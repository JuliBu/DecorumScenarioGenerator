import inspect
import itertools
import random

from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
from common.data_classes import ConditionOutput
from common.utils import check_for_inval_cond
from new_scenarios.config import DEBUG_MODE, USED_LANGUAGE


class RoomCombinationsWithWalls:
    def __init__(self, room_name: str, item_combinations):
        wall_colors = OBJ_COLORS
        self.room_name = room_name
        self.room_wall_combinations = list(itertools.product(item_combinations, wall_colors))

    def __len__(self):
        return len(self.room_wall_combinations)

    def __str__(self):
        out_str = ""
        for obj_comb, wall_color in self.room_wall_combinations:
            for obj_list in obj_comb:
                out_str = out_str + str(obj_list) + ", "
            out_str += f"{wall_color=}\n"
        return out_str

    def filter_color_and_quantity_wall(self, nr_items: int, mode: str, apply_for_all_rooms: bool = False) -> ConditionOutput:
        assert 0 <= nr_items <= 3
        assert mode in ["min", "max", "exact"]

        new_combs = []
        for obj_comb, wall_color in self.room_wall_combinations:
            if mode == "min" and obj_comb.count(wall_color) >= nr_items:
                new_combs.append((obj_comb, wall_color))
            elif mode == "max" and obj_comb.count(wall_color) <= nr_items:
                new_combs.append((obj_comb, wall_color))
            elif mode == "exact" and obj_comb.count(wall_color) == nr_items:
                new_combs.append((obj_comb, wall_color))
            else:
                raise ValueError

        check_for_inval_cond(new_combs, len(self.room_wall_combinations))
        self.room_wall_combinations = new_combs
        # if DEBUG_MODE:
        #     return f"wall_color_cond: {self.room_name=}, {nr_items=}, {mode=}"
        if apply_for_all_rooms:
            ger_output = f"In jedem Raum: {mode} {nr_items} Objekte haben die Farbe der Wand."
            eng_output = f"In every room: {mode} {nr_items} objects have the color of the wall."
        else:
            ger_output = f"In Raum {self.room_name}: {mode} {nr_items} Objekte haben die Farbe der Wand."
            eng_output = f"In room {self.room_name}: {mode} {nr_items} objects have the color of the wall."

        return ConditionOutput(eng_output, ger_output)

def get_random_method_room_with_wall():
    weighted_choices = [1, 1, 2, 2, 0, 3]
    params = {
        'nr_items': random.choice(weighted_choices),
        'color': random.choice(OBJ_COLORS),
        'mode': random.choice(["min", "max", "exact"]),
        'style': random.choice(STYLES),
        'obj_type': random.choice(OBJ_TYPES),
        'should_be_available': random.choice([True, False])
    }
    methods = [
        RoomCombinationsWithWalls.filter_color_and_quantity_wall,
    ]
    random_method = random.choice(methods)
    method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
    return random_method, method_args
