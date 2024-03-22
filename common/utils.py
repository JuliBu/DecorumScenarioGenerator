from collections import Counter
from typing import List


def check_for_inval_cond(new_combs: List, old_len: int):
    new_len = len(new_combs)
    if new_len < 1 or new_len == old_len:
        raise ValueError("Invalid condition: E.g. list would be empty or condition has no effect!")


def most_common_string(list_of_str: List[str], str_to_check: str) -> bool:
    if len(list_of_str) == 0:
        return False
    string_counts = Counter(list_of_str)
    most_common, most_count = string_counts.most_common()[0]
    sec_most_common, sec_most_count = string_counts.most_common()[1]
    return (most_common == str_to_check) and (most_count > sec_most_count)


def least_common_string(list_of_str: List[str], str_to_check: str) -> bool:
    if len(list_of_str) == 0:
        return False
    string_counts = Counter(list_of_str)
    least_common, least_count = string_counts.most_common()[-1]
    sec_least_common, sec_least_count = string_counts.most_common()[-2]
    return (least_common == str_to_check) and (least_count < sec_least_count)
