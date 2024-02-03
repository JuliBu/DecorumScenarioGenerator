from combinations.room_combinations_lvl_obj import RoomItemCombinations
from house.rooms.rooms import Room

init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")


def iter_modifications():
    bedroom1_combs = RoomItemCombinations('bedroom1')
    bedroom1_combs.filter_items_by_color_and_quantity(2, "blue", "max")
    bedroom1_combs.filter_items_by_color_and_quantity(1, "blue", "min")
    bedroom1_combs.filter_items_by_color_and_quantity(1, "red", "min")
    bedroom1_combs.filter_availability_of_type("lamp", False)
    print(len(bedroom1_combs))
    print(bedroom1_combs)


if __name__ == '__main__':
    iter_modifications()
