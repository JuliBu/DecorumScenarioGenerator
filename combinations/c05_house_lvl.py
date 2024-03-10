import inspect
import itertools
import random

from combinations.utils import get_all_rooms_and_players_from_single_house_comb
from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES, OBJ_ATTRIBUTES
from common.utils import check_for_inval_cond, most_common_string, least_common_string
from house.rooms.rooms import get_room_from_color_and_name


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

    def house_attr_most_or_least(self, attr: str, most_least: str, cond_style: str, cond_type: str, cond_color: str):
        assert attr in OBJ_ATTRIBUTES
        assert most_least in ["most", "least"]
        assert cond_color in OBJ_COLORS
        assert cond_style in STYLES
        assert cond_type in OBJ_TYPES

        new_combs = []
        for house_comb in self.house_combs:
            bedroom1_colors, bedroom2_colors, players_left, players_right, livingroom_colors, kitchen_colors = get_all_rooms_and_players_from_single_house_comb(
                house_comb)
            bedroom1 = get_room_from_color_and_name("bedroom1", bedroom1_colors)
            bedroom2 = get_room_from_color_and_name("bedroom2", bedroom2_colors)
            livingroom = get_room_from_color_and_name("livingroom", livingroom_colors)
            kitchen = get_room_from_color_and_name("kitchen", kitchen_colors)
            house_objects = []
            for room in [bedroom1, bedroom2, livingroom, kitchen]:
                for single_obj in room.get_all_objects():
                    house_objects.append(single_obj)
            objs_attr = []
            for house_obj in house_objects:
                if attr == "color":
                    objs_attr.append(house_obj.color)
                elif attr == "obj_type":
                    objs_attr.append(house_obj.obj_type)
                elif attr == "style":
                    objs_attr.append(house_obj.style)
                else:
                    raise ValueError

            if most_least == "most" and (
                    (attr == "color" and most_common_string(objs_attr, cond_color)) or
                    (attr == "obj_type" and most_common_string(objs_attr, cond_type)) or
                    (attr == "style" and most_common_string(objs_attr, cond_style))):
                new_combs.append(house_comb)
            elif most_least == "least" and (
                    (attr == "color" and least_common_string(objs_attr, cond_color)) or
                    (attr == "obj_type" and least_common_string(objs_attr, cond_type)) or
                    (attr == "style" and least_common_string(objs_attr, cond_style))):
                new_combs.append(house_comb)

        check_for_inval_cond(new_combs, len(self.house_combs))
        self.house_combs = new_combs
        # ToDo: Output
        return f"House cond, {attr=}, {most_least=}, {cond_style=}, {cond_type=}, {cond_color=}"


    def new_generic_function(self):
        # asserts
        new_combs = []
        for house_comb in self.house_combs:
            bedroom1_colors, bedroom2_colors, players_left, players_right, livingroom_colors, kitchen_colors = get_all_rooms_and_players_from_single_house_comb(
                house_comb)
            bedroom1 = get_room_from_color_and_name("bedroom1", bedroom1_colors)
            bedroom2 = get_room_from_color_and_name("bedroom2", bedroom2_colors)
            livingroom = get_room_from_color_and_name("livingroom", livingroom_colors)
            kitchen = get_room_from_color_and_name("kitchen", kitchen_colors)
            # some functions

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
            'player': random.randint(1, 4),
            'most_least': random.choice(["most", "least"])
        }
        methods = [
            self.house_color_elems,
            self.house_attr_most_or_least
        ]
        random_method = random.choice(methods)
        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)
