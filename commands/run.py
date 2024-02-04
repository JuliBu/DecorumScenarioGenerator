import random

from combinations.c01_room_combinations_lvl_obj import RoomItemCombinations
from combinations.c02_room_combinations_lvl_wall import RoomCombinationsWithWalls
from house.rooms.rooms import Room

init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")


def iter_modifications():
    # Creating rooms
    bedroom1_combs = RoomItemCombinations('bedroom1')
    bedroom2_combs = RoomItemCombinations('bedroom2')
    livingroom_combs = RoomItemCombinations('livingroom')
    kitchen_combs = RoomItemCombinations('kitchen')
    rooms_combs = [bedroom1_combs, bedroom2_combs, livingroom_combs, kitchen_combs]

    # Getting conditions on room (object) level
    while (len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs) > 10000000):
        current_room = random.choice(rooms_combs)
        print(current_room.get_random_method())
        print(len(current_room))
        print(len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs))

    # Creating wall colors for all rooms
    bedroom1_wall_combs = RoomCombinationsWithWalls(bedroom1_combs.room_name, bedroom1_combs.object_combinations)
    bedroom2_wall_combs = RoomCombinationsWithWalls(bedroom2_combs.room_name, bedroom2_combs.object_combinations)
    livingroom_wall_combs = RoomCombinationsWithWalls(livingroom_combs.room_name, livingroom_combs.object_combinations)
    kitchen_wall_combs = RoomCombinationsWithWalls(kitchen_combs.room_name, kitchen_combs.object_combinations)
    wall_comb_rooms = [bedroom1_wall_combs, bedroom2_wall_combs, livingroom_wall_combs, kitchen_wall_combs]

    # Getting conditions on room (object + wall)
    while (len(bedroom1_wall_combs) * len(bedroom2_wall_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > 10000000):
        current_room = random.choice(wall_comb_rooms)
        print(current_room.get_random_method())
        print(len(current_room))
        print(len(bedroom1_wall_combs) * len(bedroom2_wall_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))
        # bedroom1_wall_combs.filter_color_and_quantity_wall(2, "min")


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
