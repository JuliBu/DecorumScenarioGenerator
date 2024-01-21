from typing import List


def check_for_empty_list(new_combs: List):
    if len(new_combs) < 1:
        raise ValueError("List would be empty!")
