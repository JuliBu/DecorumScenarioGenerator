import inspect
import itertools
import random

from common.constants import OBJ_COLORS, POSITIONS, STYLES, OBJ_TYPES
from common.utils import check_for_empty_list
from house.objects import get_obj_style
from house.rooms.rooms import get_type_from_room_and_pos


class RoomItemCombinations:
    def __init__(self, room_name: str):
        self.object_combinations = list(itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS)))
        self.room_name = room_name

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
        return f"{self.room_name=}, {nr_items=}, {color=}, {mode=}"

    def filter_items_by_style_and_quantity(self, nr_items: int, style: str, mode: str) -> str:
        assert 0 <= nr_items <= 3
        assert style in STYLES
        assert mode in ["min", "max"]

        new_combs = []
        for obj_comb in self.object_combinations:
            # left_color, middle_color, right_color = obj_comb
            # left_type, middle_type, right_type = [get_type_from_room_and_pos(self.room_name, pos) for pos in ["left", "middle", "right"]]
            # left_style, middle_style, right_style = [get_obj_style(color, obj_type) for color, obj_type in zip([left_color, middle_color, right_color], [left_type, middle_type, right_type])]
            # styles = [left_style, middle_style, right_style]

            styles = [get_obj_style(color, get_type_from_room_and_pos(self.room_name, pos)) for color, pos in
                      zip(obj_comb, ["left", "middle", "right"])]

            if mode == "min" and styles.count(style) >= nr_items:
                new_combs.append(obj_comb)
            elif mode == "max" and styles.count(style) <= nr_items:
                new_combs.append(obj_comb)

        check_for_empty_list(new_combs)
        self.object_combinations = new_combs
        return f"{self.room_name=}, {nr_items=}, {style=}, {mode=}"

    def filter_availability_of_type(self, obj_type: str, should_be_available: bool) -> str:
        assert obj_type in OBJ_TYPES
        new_combs = []
        for obj_comb in self.object_combinations:
            left_color, middle_color, right_color = obj_comb
            left_type, middle_type, right_type = [get_type_from_room_and_pos(self.room_name, pos) for pos in ["left", "middle", "right"]]
            for obj_type, obj_color in zip([left_type, middle_type, right_type],
                                           [left_color, middle_color, right_color]):
                if obj_type == obj_type and (obj_color is not None) == should_be_available:
                    new_combs.append(obj_comb)
        check_for_empty_list(new_combs)
        self.object_combinations = new_combs
        return f"{self.room_name=}, {obj_type=}, {should_be_available=}"

    def get_random_method(self):
        params = {
            'nr_items': random.randint(0, 3),
            'color': random.choice(OBJ_COLORS),
            'mode': random.choice(["min", "max"]),
            'style': random.choice(STYLES),
            'obj_type': random.choice(OBJ_TYPES),
            'should_be_available': random.choice([True, False])
        }
        methods = [
            self.filter_items_by_color_and_quantity,
            self.filter_items_by_style_and_quantity,
            self.filter_availability_of_type
        ]
        random_method = random.choice(methods)
        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)


    def __len__(self):
        return len(self.object_combinations)

    def __str__(self):
        out_str = ""
        for obj_comb in self.object_combinations:
            for obj_list in obj_comb:
                out_str = out_str + str(obj_list) + ", "
            out_str += "\n"
        return out_str




