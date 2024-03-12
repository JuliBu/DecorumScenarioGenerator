import inspect
import itertools
import random

from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
from common.data_classes import ConditionOutput
from common.utils import check_for_inval_cond
from house.rooms import get_room_from_color_and_name


class UpperFloorCombinationsOnlyRooms:
    def __init__(self, bedroom1_combinations, bedroom2_combinations):
        self.upper_floor_combinations_only_rooms = list(itertools.product(bedroom1_combinations, bedroom2_combinations))

    def __len__(self):
        return len(self.upper_floor_combinations_only_rooms)

    def filter_floor_items_by_color_and_quantity(self, nr_items_on_floor: int, color: str, mode: str) -> ConditionOutput:
        assert 0 <= nr_items_on_floor <= 6
        assert color in OBJ_COLORS
        assert mode in ["min", "max", "equals"]

        new_combs = []
        for upper_floor in self.upper_floor_combinations_only_rooms:
            left_room, right_room = upper_floor
            color_counter = (left_room[0] + right_room[0]).count(color)
            if mode == "min" and color_counter >= nr_items_on_floor:
                new_combs.append(upper_floor)
            elif mode == "max" and color_counter <= nr_items_on_floor:
                new_combs.append(upper_floor)
            elif mode == "equals" and color_counter == nr_items_on_floor:
                new_combs.append(upper_floor)
        check_for_inval_cond(new_combs, len(self.upper_floor_combinations_only_rooms))
        self.upper_floor_combinations_only_rooms = new_combs

        if mode == "min":
            ger_output = f"In der oberen Etage müssen mindestens {nr_items_on_floor} Objekte in der Farbe {color} zu finden sein!"
            eng_output = f"In the upper floor, there must be at least {nr_items_on_floor} {color} colored objects!"
        elif mode == "max":
            ger_output = f"In der oberen Etage dürfen maximal {nr_items_on_floor} Objekte in der Farbe {color} zu finden sein!"
            eng_output = f"In the upper floor, there may be a maximum of {nr_items_on_floor} {color} colored objects!"
        elif mode == "equals":
            ger_output = f"In der oberen Etage müssen exakt {nr_items_on_floor} Objekte in der Farbe {color} zu finden sein!"
            eng_output = f"In the upper floor, there have to be exact {nr_items_on_floor} {color} colored objects!"
        else:
            raise ValueError

        return ConditionOutput(eng_output, ger_output)


    def new_generic_function(self):
        # Asserts
        new_combs = []
        for upper_floor in self.upper_floor_combinations_only_rooms:
            left_room_colors, right_room_colors = upper_floor
            bedroom1 = get_room_from_color_and_name("bedroom1", left_room_colors)
            bedroom2 = get_room_from_color_and_name("bedroom2", right_room_colors)
            # some functions




    def get_random_method(self):
        weighted_choices_items_on_floor = [
            0,
            1, 1,
            2, 2, 2,
            3, 3, 3,
            4, 4,
            5, 5,
            6
            ]
        weighted_choices_elems_in_room = [
            0,
            1, 1,
            2, 2,
            3, 3,
            4
        ]
        params = {
            'nr_items_on_floor': random.choice(weighted_choices_items_on_floor),
            'nr_elem_in_room': random.choice(weighted_choices_elems_in_room),
            'color': random.choice(OBJ_COLORS),
            'mode': random.choice(["min", "max", "equals"]),
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