import random

from combinations.c01_room_combinations_lvl_obj import RoomItemCombinations
from combinations.c02_room_combinations_lvl_wall import RoomCombinationsWithWalls
from combinations.c03_upper_floor_combinations_lvl_rooms import UpperFloorCombinationsOnlyRooms
from combinations.c04_upper_floor_combinations_lvl_players import UpperFloorCombinationsWithPlayers
from combinations.c05_house_lvl import HouseCombinations
from combinations.utils import get_rooms_and_players_from_single_upper_floor_combination_with_players, \
    get_all_rooms_and_players_from_single_house_comb
from common.constants import MAX_RETRIES
from house.rooms.rooms import Room
from new_scenarios.config import MAX_ROOM_OBJ_COMBINATIONS, MAX_ROOM_WALL_COMBINATIONS, \
    MAX_UPPER_FLOOR_ROOM_COMBINATIONS, MAX_UPPER_FLOOR_PLAYER_COMBINATIONS, MAX_HOUSE_COMBINATIONS

init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")


def iter_modifications():
    all_conds = []
    # Creating rooms
    bedroom1_combs = RoomItemCombinations('bedroom1')
    bedroom2_combs = RoomItemCombinations('bedroom2')
    livingroom_combs = RoomItemCombinations('livingroom')
    kitchen_combs = RoomItemCombinations('kitchen')
    rooms_combs = [bedroom1_combs, bedroom2_combs, livingroom_combs, kitchen_combs]

    # Getting conditions on room (object) level
    iterations = 0
    while (len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs) > MAX_ROOM_OBJ_COMBINATIONS and iterations < MAX_RETRIES):
        iterations += 1
        try:
            current_room = random.choice(rooms_combs)
            current_cond = current_room.get_random_method()
            print(current_cond)
            all_conds.append(current_cond)
            print(len(current_room))
            print(len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs))
        except ValueError as e:
            print(f"{e}")

    # Creating wall colors for all rooms
    bedroom1_wall_combs = RoomCombinationsWithWalls(bedroom1_combs.room_name, bedroom1_combs.object_combinations)
    bedroom2_wall_combs = RoomCombinationsWithWalls(bedroom2_combs.room_name, bedroom2_combs.object_combinations)
    livingroom_wall_combs = RoomCombinationsWithWalls(livingroom_combs.room_name, livingroom_combs.object_combinations)
    kitchen_wall_combs = RoomCombinationsWithWalls(kitchen_combs.room_name, kitchen_combs.object_combinations)
    wall_comb_rooms = [bedroom1_wall_combs, bedroom2_wall_combs, livingroom_wall_combs, kitchen_wall_combs]

    # Getting conditions on room (object + wall)
    while (len(bedroom1_wall_combs) * len(bedroom2_wall_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > MAX_ROOM_WALL_COMBINATIONS and iterations < MAX_RETRIES):
        iterations += 1
        try:
            current_room = random.choice(wall_comb_rooms)
            current_cond = current_room.get_random_method()
            print(current_cond)
            all_conds.append(current_cond)
            print(len(current_room))
            print(len(bedroom1_wall_combs) * len(bedroom2_wall_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))
        except ValueError as e:
            print(f"{e}")

    # Creating conditions for upper floor
    upper_floor_combs = UpperFloorCombinationsOnlyRooms(bedroom1_wall_combs.room_wall_combinations, bedroom2_wall_combs.room_wall_combinations)
    while (len(upper_floor_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > MAX_UPPER_FLOOR_ROOM_COMBINATIONS and iterations < MAX_RETRIES):
        iterations += 1
        try:
            current_cond = upper_floor_combs.get_random_method()
            print(current_cond)
            all_conds.append(current_cond)
            print(len(upper_floor_combs))
            print(len(upper_floor_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))

        except ValueError as e:
            print(f"{e}")

    # Creating player conditions
    upper_floor_player_combs = UpperFloorCombinationsWithPlayers(upper_floor_combs.upper_floor_combinations_only_rooms)
    while (len(upper_floor_player_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > MAX_UPPER_FLOOR_PLAYER_COMBINATIONS and iterations < MAX_RETRIES):
        iterations += 1
        try:
            current_cond = upper_floor_player_combs.get_random_method()
            print(current_cond)
            all_conds.append(current_cond)
            print(len(upper_floor_player_combs))
            print(len(upper_floor_player_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))

        except ValueError as e:
            print(f"{e}")

    # Creating house conditions
    house_combs = HouseCombinations(upper_floor_player_combs.upper_floor_combinations_with_players, livingroom_wall_combs.room_wall_combinations, kitchen_wall_combs.room_wall_combinations)
    while len(house_combs) > MAX_HOUSE_COMBINATIONS and iterations < MAX_RETRIES:
        iterations += 1
        try:
            current_cond = house_combs.get_random_method()
            print(current_cond)
            all_conds.append(current_cond)
            print(len(house_combs))

        except ValueError as e:
            print(f"{e}")


    print("\n\nAll conditions:\n")
    for cond in all_conds:
        print(cond)

    print(f"Number of conditions: {len(all_conds)}")
    print(f"possible solutions: {len(house_combs)}")
    print("\nOne possible solution:\n")
    out_bedroom1, out_bedroom2, players_left, players_right, livingroom, kitchen = get_all_rooms_and_players_from_single_house_comb(house_combs.house_combs[0])
    for room in [out_bedroom1, out_bedroom2, livingroom, kitchen]:
        print(room)
    for players in [players_left, players_right]:
        print(players)


if __name__ == '__main__':
    iter_modifications()
