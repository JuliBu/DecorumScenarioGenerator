import inspect
import itertools
import random

from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
from common.utils import check_for_inval_cond


def get_rooms_and_players_from_comb(single_upper_floor_combination_with_players):
    bedroom1 = single_upper_floor_combination_with_players[0][0]
    bedroom2 = single_upper_floor_combination_with_players[0][1]
    players_left = single_upper_floor_combination_with_players[1][0]
    players_right = single_upper_floor_combination_with_players[1][1]
    return bedroom1, bedroom2, players_left, players_right


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

    def __len__(self):
        return len(self.upper_floor_combinations_with_players)

    def player_color_elem_in_room(self, player: int, nr_items: int, color: str, mode: str):
        assert 0 <= nr_items <= 6
        assert color in OBJ_COLORS
        assert mode in ["min", "max"]

        new_combs = []
        for upper_floor_comb in self.upper_floor_combinations_with_players:
            bedroom1, bedroom2, players_left, players_right = get_rooms_and_players_from_comb(upper_floor_comb)
            if player in players_left:
                color_counter = bedroom1[0].count(color)
                if bedroom1[1] == color:
                    color_counter += 1
            elif player in players_right:
                color_counter = bedroom2[0].count(color)
                if bedroom2[1] == color:
                    color_counter += 1
            else:
                raise KeyError(f"{player=} not in any room!")

            if mode == "min" and color_counter >= nr_items:
                new_combs.append(upper_floor_comb)
            elif mode == "max" and color_counter <= nr_items:
                new_combs.append(upper_floor_comb)
        check_for_inval_cond(new_combs, len(self.upper_floor_combinations_with_players))
        self.upper_floor_combinations_with_players = new_combs
        return f"Players cond, {player=}, {nr_items=}, {color=}, {mode=}"

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
            'should_be_available': random.choice([True, False]),
            'player': random.randint(1,4)
        }
        methods = [
            self.player_color_elem_in_room,
        ]
        random_method = random.choice(methods)
        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)
