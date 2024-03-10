import random
from typing import List, Tuple

from common.data_classes import ConditionOutput


def split_conds_to_4_players(unsorted_conds: List[ConditionOutput]) -> Tuple[List[ConditionOutput], List[ConditionOutput], List[ConditionOutput], List[ConditionOutput]]:
    player_conds = {player: [] for player in range(5)}
    unassigned_conds = []
    for cond in unsorted_conds:
        if cond.specific_player is not None:
            # -1, as the player goes form 1-4 and the indexes from 0-3
            player_conds[cond.specific_player-1].append(cond)
        else:
            unassigned_conds.append(cond)
    random.shuffle(unassigned_conds)

    nr_conds_per_player = 0
    while len(unassigned_conds) > 0:
        nr_conds_per_player += 1
        for i in range(4):
            if not len(unassigned_conds) > 0:
                break
            if len(player_conds[i]) < nr_conds_per_player:
                player_conds[i].append(unassigned_conds.pop())

    return player_conds[0], player_conds[1], player_conds[2], player_conds[3]




