import inspect
import itertools
import random

from combinations.utils import get_rooms_and_players_from_single_upper_floor_combination_with_players
from common.constants import OBJ_COLORS, STYLES, OBJ_TYPES
from common.data_classes import ConditionOutput
from common.utils import check_for_inval_cond
from house.rooms.rooms import get_room_from_color_and_name
from new_scenarios.config import DEBUG_MODE, USED_LANGUAGE


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

    def player_color_elem_in_room(self, player: int, nr_elems_0_to_4: int, color: str, mode: str) -> ConditionOutput:
        assert 0 <= nr_elems_0_to_4 <= 4
        assert color in OBJ_COLORS
        assert mode in ["min", "max"]

        new_combs = []
        for upper_floor_comb in self.upper_floor_combinations_with_players:
            bedroom1, bedroom2, players_left, players_right = get_rooms_and_players_from_single_upper_floor_combination_with_players(
                upper_floor_comb)
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

            if mode == "min" and color_counter >= nr_elems_0_to_4:
                new_combs.append(upper_floor_comb)
            elif mode == "max" and color_counter <= nr_elems_0_to_4:
                new_combs.append(upper_floor_comb)
        check_for_inval_cond(new_combs, len(self.upper_floor_combinations_with_players))
        self.upper_floor_combinations_with_players = new_combs

        if mode == "min":
            ger_output = f"In deinem Zimmern müssen mindestens {nr_elems_0_to_4} Elemente der Farbe {color} angehören!"
            eng_output = f"In your rooms, there must be at least {nr_elems_0_to_4} elements belonging to the color {color}!"
        elif mode == "max":
            ger_output = f"In deinem Zimmern dürfen höchstens {nr_elems_0_to_4} Elemente der Farbe {color} angehören!"
            eng_output = f"In your rooms, there may be at most {nr_elems_0_to_4} elements belonging to the color {color}!"
        else:
            raise ValueError
        return ConditionOutput(eng_output, ger_output, player)

    def player_a_avoids_player_b(self, player: int, player_b: int):
        assert player in [1, 2, 3, 4]
        assert player_b in [1, 2, 3, 4]
        assert player != player_b

        new_combs = []
        for upper_floor_comb in self.upper_floor_combinations_with_players:
            bedroom1_colors, bedroom2_colors, players_left, players_right = get_rooms_and_players_from_single_upper_floor_combination_with_players(
                upper_floor_comb)
            if (player in players_left and player_b not in players_left) or (player in players_right and player_b not in players_right):
                new_combs.append(upper_floor_comb)

        ger_output = f"Du teilst dir kein Zimmer mit Spieler {player_b}."
        eng_output = f"You do not share a room with Player {player_b}."
        return ConditionOutput(eng_output, ger_output, player)


    def new_generic_function(self):
        # asserts
        new_combs = []
        for upper_floor_comb in self.upper_floor_combinations_with_players:
            bedroom1_colors, bedroom2_colors, players_left, players_right = get_rooms_and_players_from_single_upper_floor_combination_with_players(
                upper_floor_comb)
            bedroom1 = get_room_from_color_and_name("bedroom1", bedroom1_colors)
            bedroom2 = get_room_from_color_and_name("bedroom2", bedroom2_colors)
            # some functions

    def get_random_method(self):
        weighted_choices_0_to_6 = [
            0,
            1, 1,
            2, 2, 2,
            3, 3, 3,
            4, 4,
            5, 5,
            6
            ]
        weighted_choices_0_to_3 = [
            0,
            1, 1,
            2, 2,
            3
            ]
        weighted_choices_0_to_4 = [
            0,
            1, 1,
            2, 2, 2,
            3, 3,
            4
            ]
        player_a = random.choice([1, 2, 3, 4])
        player_b = random.choice(list({1, 2, 3, 4} - {player_a}))
        params = {
            'nr_items_0_to_6': random.choice(weighted_choices_0_to_6),
            'nr_items_0_to_3': random.choice(weighted_choices_0_to_3),
            'nr_elems_0_to_4': random.choice(weighted_choices_0_to_4),
            'color': random.choice(OBJ_COLORS),
            'mode': random.choice(["min", "max"]),
            'style': random.choice(STYLES),
            'obj_type': random.choice(OBJ_TYPES),
            'should_be_available': random.choice([True, False]),
            'player': player_a,
            'player_b': player_b
        }
        methods_with_weights = [
            (self.player_color_elem_in_room, 15),
            (self.player_a_avoids_player_b, 1),
        ]
        total_weight = sum(weight for method, weight in methods_with_weights)
        random_number = random.uniform(0, total_weight)
        cumulative_weight = 0

        for method, weight in methods_with_weights:
            cumulative_weight += weight
            if random_number < cumulative_weight:
                random_method = method
                break

        method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
        return random_method(**method_args)
