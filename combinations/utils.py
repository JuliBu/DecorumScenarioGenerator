from typing import List
import random

from common.constants import OBJ_ATTRIBUTES, STYLES, OBJ_TYPES, OBJ_COLORS
from common.data_classes import MethodWithWeight


def get_rooms_and_players_from_single_upper_floor_combination_with_players(single_upper_floor_combination_with_players):
    bedroom1 = single_upper_floor_combination_with_players[0][0]
    bedroom2 = single_upper_floor_combination_with_players[0][1]
    players_left = single_upper_floor_combination_with_players[1][0]
    players_right = single_upper_floor_combination_with_players[1][1]
    return bedroom1, bedroom2, players_left, players_right


def get_all_rooms_and_players_from_single_house_comb(single_house_comb):
    bedroom1, bedroom2, players_left, players_right = get_rooms_and_players_from_single_upper_floor_combination_with_players(single_house_comb[0])
    livingroom = single_house_comb[1]
    kitchen = single_house_comb[2]
    return bedroom1, bedroom2, players_left, players_right, livingroom, kitchen


def get_attr_value(attribute: str, obj_style: str, obj_type: str, obj_color: str) -> str:
    assert attribute in OBJ_ATTRIBUTES
    assert obj_style in STYLES
    assert obj_type in OBJ_TYPES
    assert obj_color in OBJ_COLORS + [None]

    if attribute == "style":
        return obj_style
    elif attribute == "obj_type":
        return obj_type
    elif attribute == "color":
        return obj_color
    else:
        raise NotImplementedError


def get_weighted_random_method(methods_with_weights: List[MethodWithWeight]):
    total_weight = sum(method_with_weight.weight for method_with_weight in methods_with_weights)
    random_number = random.uniform(0, total_weight)
    cumulative_weight = 0

    for method_with_weight in methods_with_weights:
        cumulative_weight += method_with_weight.weight
        if random_number < cumulative_weight:
            return method_with_weight.method
