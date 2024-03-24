import random

from src.combinations.c01_room_combinations_lvl_obj import RoomItemCombinations
from src.combinations.c02_room_combinations_lvl_wall import RoomCombinationsWithWalls
from src.combinations.c03_upper_floor_combinations_lvl_rooms import UpperFloorCombinationsOnlyRooms
from src.combinations.c04_upper_floor_combinations_lvl_players import UpperFloorCombinationsWithPlayers
from src.combinations.c05_house_lvl import HouseCombinations
from src.combinations.utils import get_all_rooms_and_players_from_single_house_comb
from src.house.rooms import Room
from new_scenarios.config import SET_SEED, SHOW_PRINTS
from src.ui.conditions import split_conds_to_4_players
from src.ui.pdf_gen import gen_pdf_version

random.seed(SET_SEED)

init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")


def iter_modifications(gen_id: int):
    all_conds = []
    # Creating rooms
    bedroom1_combs = RoomItemCombinations('bedroom1')
    bedroom2_combs = RoomItemCombinations('bedroom2')
    livingroom_combs = RoomItemCombinations('livingroom')
    kitchen_combs = RoomItemCombinations('kitchen')
    rooms_combs = [bedroom1_combs, bedroom2_combs, livingroom_combs, kitchen_combs]

    # Getting conditions on room (object) level
    iterations = 0
    nr_room_combs = len(bedroom1_combs) * len(bedroom2_combs) * len(livingroom_combs) * len(kitchen_combs)

    # Room Level
    livingroom_combs.filter_if_x_avail_then_y_avail("color", "obj_type", "yellow", "rare", "curiosity", True, False)
    bedroom1_combs.filter_if_x_avail_then_y_avail("obj_type", "color", "yellow", "rare", "lamp", True, False)
    bedroom1_combs.filter_items_by_color_and_quantity(2, "green", "min", False)
    bedroom2_combs.filter_items_by_color_and_quantity(2, "green", "min", False)
    livingroom_combs.filter_items_by_color_and_quantity(2, "green", "min", False)
    kitchen_combs.filter_items_by_color_and_quantity(2, "green", "min", False)
    kitchen_combs.filter_availability_of_type("lamp", False, False)


    # Creating wall colors for all rooms
    bedroom1_wall_combs = RoomCombinationsWithWalls(bedroom1_combs.room_name, bedroom1_combs.object_combinations)
    bedroom2_wall_combs = RoomCombinationsWithWalls(bedroom2_combs.room_name, bedroom2_combs.object_combinations)
    livingroom_wall_combs = RoomCombinationsWithWalls(livingroom_combs.room_name, livingroom_combs.object_combinations)
    kitchen_wall_combs = RoomCombinationsWithWalls(kitchen_combs.room_name, kitchen_combs.object_combinations)
    wall_comb_rooms = [bedroom1_wall_combs, bedroom2_wall_combs, livingroom_wall_combs, kitchen_wall_combs]

    # Getting conditions on room (object + wall)
    # Wall level

    # Creating conditions for upper floor
    upper_floor_combs = UpperFloorCombinationsOnlyRooms(bedroom1_wall_combs.room_wall_combinations, bedroom2_wall_combs.room_wall_combinations)
    # Upper floor level


    # Creating player conditions
    upper_floor_player_combs = UpperFloorCombinationsWithPlayers(upper_floor_combs.upper_floor_combinations_only_rooms)
    # Player level
    upper_floor_player_combs.player_color_elem_in_room(1,1,"yellow","min")
    upper_floor_player_combs.player_color_elem_in_room(2, 1, "blue", "min")
    upper_floor_player_combs.player_color_elem_in_room(2, 2, "green", "max")
    upper_floor_player_combs.player_color_elem_in_room(4, 2, "red", "min")



    # Creating house conditions
    house_combs = HouseCombinations(upper_floor_player_combs.upper_floor_combinations_with_players, livingroom_wall_combs.room_wall_combinations, kitchen_wall_combs.room_wall_combinations)
    house_combs.house_color_elems(1, "yellow", "max")
    house_combs.house_attr_most_or_least("obj_type", "most", "rare", "curiosity", "red")
    house_combs.house_color_elems(10, "green", "min")
    house_combs.house_attr_most_or_least("style", "least", "rare", "lamp", "red")

    if SHOW_PRINTS:
        print("\n\nAll conditions:\n")
        for cond in all_conds:
            print(cond)

    if len(all_conds) == 12:
        print(f"Found a solution with 12 conditions: {SET_SEED}_{gen_id}!\n")
        gen_pdf_version(all_conds, f"../new_scenarios/pdfs/ger_{str(SET_SEED)}_{str(gen_id)}.pdf", f"{SET_SEED}_{gen_id}", len(house_combs), "ger")
        gen_pdf_version(all_conds, f"../new_scenarios/pdfs/eng_{str(SET_SEED)}_{str(gen_id)}.pdf", f"{SET_SEED}_{gen_id}", len(house_combs), "eng")
    player_1_conds, player_2_conds, player_3_conds, player_4_conds = split_conds_to_4_players(all_conds)
    for idx, player_conds in enumerate([player_1_conds, player_2_conds, player_3_conds, player_4_conds]):
        if SHOW_PRINTS:
            print(f"\nPlayer {idx+1}:")
            for cond in player_conds:
                print(cond)

    if SHOW_PRINTS:
        print(f"Number of conditions: {len(all_conds)}")
        print(f"possible solutions: {len(house_combs)}")
        print("\nOne possible solution:\n")
        out_bedroom1, out_bedroom2, players_left, players_right, livingroom, kitchen = get_all_rooms_and_players_from_single_house_comb(house_combs.house_combs[0])
        for room in [out_bedroom1, out_bedroom2, livingroom, kitchen]:
            print(room)
        for players in [players_left, players_right]:
            print(players)


def process_iteration(idx):
    try:
        iter_modifications(idx)
        return idx, None
    except TimeoutError:
        return idx, TimeoutError


if __name__ == "__main__":

    process_iteration(1)
