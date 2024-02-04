import random

from combinations.room_combinations_lvl_obj import RoomItemCombinations, RoomCombinationsWithWalls
from house.rooms.rooms import Room

init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")


def iter_modifications():
    bedroom1_combs = RoomItemCombinations('bedroom1')
    bedroom2_combs = RoomItemCombinations('bedroom2')
    livingroom_combs = RoomItemCombinations('livingroom')
    kitchen_combs = RoomItemCombinations('kitchen')
    rooms_combs = [bedroom1_combs, bedroom2_combs, livingroom_combs, kitchen_combs]
    # bedroom1_combs.filter_items_by_color_and_quantity(2, "blue", "max")
    # bedroom1_combs.filter_items_by_color_and_quantity(1, "blue", "min")
    # bedroom1_combs.filter_items_by_color_and_quantity(1, "red", "min")
    # bedroom1_combs.filter_availability_of_type("lamp", False)

    while (len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs) > 10000000):
        current_room = random.choice(rooms_combs)
        print(current_room.get_random_method())
        print(len(current_room))
        print(len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs))

    bedroom1_wall_combs = RoomCombinationsWithWalls(bedroom1_combs.room_name, bedroom1_combs.object_combinations)
    bedroom2_wall_combs = RoomCombinationsWithWalls(bedroom2_combs.room_name, bedroom2_combs.object_combinations)
    livingroom_wall_combs = RoomCombinationsWithWalls(livingroom_combs.room_name, livingroom_combs.object_combinations)
    kitchen_wall_combs = RoomCombinationsWithWalls(kitchen_combs.room_name, kitchen_combs.object_combinations)

    bedroom1_wall_combs.filter_color_and_quantity_wall(2, "min")


    #ToDo: Debug -> why 3 list entries?
    """
    nr_items=2, color='blue', mode='max'
obj_type='lamp', should_be_available=True
nr_items=3, color='red', mode='min'
nr_items=3, color='green', mode='max'
"""

    # print(bedroom1_combs)


if __name__ == '__main__':
    iter_modifications()
