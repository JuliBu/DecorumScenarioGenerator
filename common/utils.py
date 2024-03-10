from collections import Counter
from typing import List


def check_for_inval_cond(new_combs: List, old_len: int):
    new_len = len(new_combs)
    if new_len < 1 or new_len == old_len:
        raise ValueError("Invalid condition: E.g. list would be empty or condition has no effect!")


def most_common_string(list_of_str: List[str], str_to_check: str) -> bool:
    string_counts = Counter(list_of_str)
    most_common, count = string_counts.most_common(1)[0]
    return most_common == str_to_check


def least_common_string(list_of_str: List[str], str_to_check: str) -> bool:
    string_counts = Counter(list_of_str)
    least_common, count = string_counts.most_common()[-1]
    return least_common == str_to_check
