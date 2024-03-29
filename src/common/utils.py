from collections import Counter
from typing import List


def check_for_inval_cond(new_combs: List, old_len: int):
    new_len = len(new_combs)
    if new_len > old_len:
        raise AssertionError
    if new_len < 1 or new_len == old_len:
        raise ValueError("Invalid condition: E.g. list would be empty or condition has no effect!")


def count_string_occurrences(list_of_str: List[str], possible_values: List[str]) -> Counter:
    string_counter = Counter()
    for string in list_of_str:
        if string in possible_values:
            string_counter[string] += 1
    return string_counter


def most_common_string(list_of_str: List[str], str_to_check: str, possible_values: List[str]) -> bool:
    if len(list_of_str) == 0:
        return False
    str_counter = count_string_occurrences(list_of_str, possible_values)
    for possible_value in possible_values:
        if str_counter[possible_value] >= str_counter[str_to_check] and possible_value != str_to_check:
            return False
    return True


def least_common_string(list_of_str: List[str], str_to_check: str, possible_values: List[str]) -> bool:
    if len(list_of_str) == 0:
        return False
    str_counter = count_string_occurrences(list_of_str, possible_values)
    for possible_value in possible_values:
        if str_counter[possible_value] <= str_counter[str_to_check] and possible_value != str_to_check:
            return False
    return True
