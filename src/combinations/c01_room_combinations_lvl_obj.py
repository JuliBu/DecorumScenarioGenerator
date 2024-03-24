import inspect
import itertools
import random

from src.combinations.utils import get_attr_value, get_weighted_random_method
from src.common.constants import OBJ_COLORS, POSITIONS, STYLES, OBJ_TYPES, OBJ_ATTRIBUTES
from src.common.data_classes import ConditionOutput, MethodWithWeight
from src.common.utils import check_for_inval_cond
from src.house.objects import get_obj_style
from src.house.rooms import get_type_from_room_and_pos


class RoomItemCombinations:
    def __init__(self, room_name: str):
        self.object_combinations = list(itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS)))
        self.room_name = room_name

    def filter_items_by_color_and_quantity(self, nr_items: int, color: str, mode: str, apply_for_all_rooms: bool = False) -> ConditionOutput:
        assert 0 <= nr_items <= 3
        assert color in OBJ_COLORS
        assert mode in ["min", "max"]

        new_combs = []
        for obj_comb in self.object_combinations:
            if mode == "min" and obj_comb.count(color) >= nr_items:
                new_combs.append(obj_comb)
            elif mode == "max" and obj_comb.count(color) <= nr_items:
                new_combs.append(obj_comb)

        check_for_inval_cond(new_combs, len(self.object_combinations))
        self.object_combinations = new_combs
        # if DEBUG_MODE:
        #     return f"{self.room_name=}, {nr_items=}, {color=}, {mode=}"
        if apply_for_all_rooms:
            ger_output = f"In jedem Raum: {mode} {nr_items} Objekte mit der Farbe {color}."
            eng_output = f"In every room: {mode} {nr_items} objects in color {color}"
        else:
            ger_output = f"In Raum {self.room_name}: {mode} {nr_items} Objekte mit der Farbe {color}."
            eng_output = f"In room {self.room_name}: {mode} {nr_items} objects in color {color}"

        return ConditionOutput(eng_output, ger_output)

    def filter_items_by_style_and_quantity(self, nr_items: int, style: str, mode: str, apply_for_all_rooms: bool = False) -> ConditionOutput:
        assert 0 <= nr_items <= 3
        assert style in STYLES
        assert mode in ["min", "max"]

        new_combs = []
        for obj_comb in self.object_combinations:
            # left_color, middle_color, right_color = obj_comb
            # left_type, middle_type, right_type = [get_type_from_room_and_pos(self.room_name, pos) for pos in ["left", "middle", "right"]]
            # left_style, middle_style, right_style = [get_obj_style(color, obj_type) for color, obj_type in zip([left_color, middle_color, right_color], [left_type, middle_type, right_type])]
            # styles = [left_style, middle_style, right_style]

            styles = [get_obj_style(color, get_type_from_room_and_pos(self.room_name, pos)) for color, pos in
                      zip(obj_comb, ["left", "middle", "right"])]

            if mode == "min" and styles.count(style) >= nr_items:
                new_combs.append(obj_comb)
            elif mode == "max" and styles.count(style) <= nr_items:
                new_combs.append(obj_comb)

        check_for_inval_cond(new_combs, len(self.object_combinations))
        self.object_combinations = new_combs
        # if DEBUG_MODE:
        #     return f"{self.room_name=}, {nr_items=}, {style=}, {mode=}"

        if apply_for_all_rooms:
            ger_output = f"In jedem Raum: {mode} {nr_items} Objekte mit dem Stil {style}."
            eng_output = f"In every room: {mode} {nr_items} objects with style {style}"
        else:
            ger_output = f"In Raum {self.room_name}: {mode} {nr_items} Objekte mit dem Stil {style}."
            eng_output = f"In room {self.room_name}: {mode} {nr_items} objects with style {style}"

        return ConditionOutput(eng_output, ger_output)

    def filter_availability_of_type(self, obj_type: str, should_be_available: bool, apply_for_all_rooms: bool = False) -> ConditionOutput:
        assert obj_type in OBJ_TYPES
        new_combs = []
        for obj_comb in self.object_combinations:
            append_this_comb = False
            left_color, middle_color, right_color = obj_comb
            left_type, middle_type, right_type = [get_type_from_room_and_pos(self.room_name, pos) for pos in ["left", "middle", "right"]]
            for obj_type_iter, obj_color in zip([left_type, middle_type, right_type],
                                           [left_color, middle_color, right_color]):
                if obj_type_iter == obj_type and (obj_color is not None) == should_be_available:
                    append_this_comb = True
                    break
            if append_this_comb:
                new_combs.append(obj_comb)
        check_for_inval_cond(new_combs, len(self.object_combinations))
        self.object_combinations = new_combs
        # if DEBUG_MODE:
        #     return f"{self.room_name=}, {obj_type=}, {should_be_available=}"
        if apply_for_all_rooms:
            if should_be_available:
                ger_output = f"In jedem Raum muss ein Objekt des Typs {obj_type} vorhanden sein."
                eng_output = f"In every single room, there has to be an object of type {obj_type}."
            else:
                ger_output = f"In keinem Raum darf ein Objekt des Typs {obj_type} vorhanden sein."
                eng_output = f"In every single room, there has to be no object of type {obj_type}."
        else:
            if should_be_available:
                ger_output = f"In Raum {self.room_name} muss ein Objekt des Typs {obj_type} vorhanden sein."
                eng_output = f"In room {self.room_name}, there has to be an object of type {obj_type}."

            else:
                ger_output = f"In Raum {self.room_name} darf kein Objekt des Typs {obj_type} vorhanden sein."
                eng_output = f"In room {self.room_name}, there has to be no object of type {obj_type}."
        return ConditionOutput(eng_output, ger_output)

    def filter_if_x_avail_then_y_avail(self, obj_attr1: str, obj_attr2: str, color: str, style: str, obj_type: str, should_be_available: bool, apply_for_all_rooms: bool = False) -> ConditionOutput:
        assert obj_type in OBJ_TYPES
        assert style in STYLES
        assert color in OBJ_COLORS
        assert obj_attr1 in OBJ_ATTRIBUTES
        assert obj_attr2 in OBJ_ATTRIBUTES

        new_combs = []
        for obj_comb in self.object_combinations:
            append_this_comb = False
            left_color, middle_color, right_color = obj_comb
            left_type, middle_type, right_type = [get_type_from_room_and_pos(self.room_name, pos) for pos in ["left", "middle", "right"]]
            left_style, middle_style, right_style = [get_obj_style(color, obj_type) for color, obj_type in
                                                     zip([left_color, middle_color, right_color],
                                                         [left_type, middle_type, right_type])]
            if obj_attr1 == "color":
                first_part_fulfilled = color in [left_color, middle_color, right_color]
            elif obj_attr1 == "obj_type":
                first_part_fulfilled = obj_type in [left_type, middle_type, right_type]
            elif obj_attr1 == "style":
                first_part_fulfilled = style in [left_style, middle_style, right_style]
            else:
                raise NotImplementedError(f"{obj_attr1=} not recognized")

            if not first_part_fulfilled:
                append_this_comb = True
            else:
                for obj_type_iter, obj_color_iter, obj_style_iter in zip([left_type, middle_type, right_type],
                                                                         [left_color, middle_color, right_color],
                                                                         [left_style, middle_style, right_style]):
                    if obj_attr2 == "color":
                        if obj_color_iter == color and should_be_available:
                            append_this_comb = True
                            break
                        elif obj_color_iter == color and not should_be_available:
                            append_this_comb = False
                            break
                    elif obj_attr2 == "style":
                        if obj_style_iter == style and obj_color_iter is not None and should_be_available:
                            append_this_comb = True
                            break
                        elif obj_style_iter == style and obj_color_iter is not None and not should_be_available:
                            append_this_comb = False
                            break
                    elif obj_attr2 == "obj_type":
                        if obj_type_iter == obj_type and obj_color_iter is not None and should_be_available:
                            append_this_comb = True
                            break
                        elif obj_type_iter == obj_type and obj_color_iter is not None and not should_be_available:
                            append_this_comb = False
                            break
            if append_this_comb:
                new_combs.append(obj_comb)
        check_for_inval_cond(new_combs, len(self.object_combinations))
        self.object_combinations = new_combs
        # if DEBUG_MODE:
        #     return f"{obj_attr1=}, {obj_attr2=}, {self.room_name=}, {color=}, {style=}  {obj_type=}, {should_be_available=}"
        attr_value_1 = get_attr_value(obj_attr1, style, obj_type, color)
        attr_value_2 = get_attr_value(obj_attr2, style, obj_type, color)

        if apply_for_all_rooms:
            if should_be_available:
                ger_output = f"Für jeden Raum gilt: Wenn mind. 1 Objekt von {obj_attr1} = {attr_value_1} vorhanden ist," \
                           f" muss auch ein Objekt von {obj_attr2} = {attr_value_2} vorhanden sein."
                eng_output = f"In each room: If at least 1 object has {obj_attr1} = {attr_value_1}," \
                             f" then there must also be an object with {obj_attr2} = {attr_value_2}."
            else:
                ger_output = f"Für jeden Raum gilt: Wenn mind. 1 Objekt von {obj_attr1} = {attr_value_1} vorhanden ist," \
                           f" darf kein Objekt von {obj_attr2} = {attr_value_2} vorhanden sein."
                eng_output = f"For each room, it applies: If at least 1 object has {obj_attr1} = {attr_value_1}," \
                           f" then no object with {obj_attr2} = {attr_value_2} must be present."
        else:
            if should_be_available:
                ger_output = f"Für Raum {self.room_name} gilt: Wenn mind. 1 Objekt von {obj_attr1} = {attr_value_1} vorhanden ist," \
                       f" muss auch ein Objekt von {obj_attr2} = {attr_value_2} vorhanden sein."
                eng_output = f"For room {self.room_name}, it applies: If at least 1 object has {obj_attr1} = {attr_value_1}," \
                             f" then there must also be an object with {obj_attr2} = {attr_value_2}."
            else:
                ger_output = f"Für Raum {self.room_name} gilt: Wenn mind. 1 Objekt von {obj_attr1} = {attr_value_1} vorhanden ist," \
                       f" darf kein Objekt von {obj_attr2} = {attr_value_2} vorhanden sein."
                eng_output = f"For room {self.room_name}, it applies: If at least 1 object has {obj_attr1} = {attr_value_1}," \
                             f" then no object with {obj_attr2} = {attr_value_2} must be present."

        return ConditionOutput(eng_output, ger_output)

    def __len__(self):
        return len(self.object_combinations)

    def __str__(self):
        out_str = ""
        for obj_comb in self.object_combinations:
            for obj_list in obj_comb:
                out_str = out_str + str(obj_list) + ", "
            out_str += "\n"
        return out_str


def get_random_method_room_obj():
    weighted_choices = [1, 1, 2, 2, 0, 3]
    weighted_min_max = ["min", "max", "max"]
    obj_attr1 = random.choice(OBJ_ATTRIBUTES)
    obj_attr2 = random.choice(list(set(OBJ_ATTRIBUTES) - {obj_attr1}))
    params = {
        'nr_items': random.choice(weighted_choices),
        'color': random.choice(OBJ_COLORS),
        'mode': random.choice(weighted_min_max),
        'style': random.choice(STYLES),
        'obj_type': random.choice(OBJ_TYPES),
        'should_be_available': random.choice([True, False]),
        'obj_attr1': obj_attr1,
        'obj_attr2': obj_attr2,
    }
    methods_with_weights = [
        MethodWithWeight(RoomItemCombinations.filter_items_by_color_and_quantity, 5),
        MethodWithWeight(RoomItemCombinations.filter_availability_of_type, 5),
        MethodWithWeight(RoomItemCombinations.filter_if_x_avail_then_y_avail, 5),
        MethodWithWeight(RoomItemCombinations.filter_if_x_avail_then_y_avail, 5),
    ]
    random_method = get_weighted_random_method(methods_with_weights)
    method_args = {param: params[param] for param in params if param in inspect.signature(random_method).parameters}
    return random_method, method_args





