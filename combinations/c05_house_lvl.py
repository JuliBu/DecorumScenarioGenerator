import inspect
import itertools
import random

from combinations.utils import get_all_rooms_and_players_from_single_house_comb
from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
from common.utils import check_for_inval_cond


class HouseCombinations:
    def __init__(self, upper_floor_combinations_with_players, living_room_combs, kitchen_combs):
        self.house_combs = list(itertools.product(upper_floor_combinations_with_players, living_room_combs, kitchen_combs))

    def __len__(self):
        return len(self.house_combs)

    def house_color_elems(self, nr_elems_in_house: int, color: str, mode: str):
        assert 0 <= nr_elems_in_house <= 16
        assert color in OBJ_COLORS
        assert mode in ["min", "max"]

        new_combs = []
        for house_comb in self.house_combs:
            bedroom1, bedroom2, players_left, players_right, livingroom, kitchen = get_all_rooms_and_players_from_single_house_comb(house_comb)
            color_counter = 0
            for room in [bedroom1, bedroom2, livingroom, kitchen]:
                color_counter += room[0].count(color)
                if room[1] == color:
                    color_counter += 1
            if mode == "min" and color_counter >= nr_elems_in_house:
                new_combs.append(house_comb)
            elif mode == "max" and color_counter <= nr_elems_in_house:
                new_combs.append(house_comb)
        check_for_inval_cond(new_combs, len(self.house_combs))
        self.house_combs = new_combs
        return f"House cond, {nr_elems_in_house=}, {color=}, {mode=}"

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
            'nr_elems_in_house': random.randint(0, 16),
            'color': random.choice(OBJ_COLORS),
            'mode': random.choice(["min", "max"]),
            'style': random.choice(STYLES),
            'obj_type': random.choice(OBJ_TYPES),
            'should_be_available': random.choice([True, False]),
            'player': random.randint(1, 4)
        }
        methods = [
            self.house_color_elems,
        ]
        random_method = random.choice(methods)
        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)
