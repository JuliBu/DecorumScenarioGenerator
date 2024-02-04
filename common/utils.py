from typing import List


def check_for_inval_cond(new_combs: List, old_len: int):
    new_len = len(new_combs)
    if new_len < 1 or new_len == old_len:
        raise ValueError("Invalid condition: E.g. list would be empty or condition has no effect!")
