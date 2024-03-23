import concurrent.futures
import multiprocessing
import random
from copy import deepcopy

from tqdm import tqdm

from combinations.c01_room_combinations_lvl_obj import RoomItemCombinations, get_random_method_room_obj
from combinations.c02_room_combinations_lvl_wall import RoomCombinationsWithWalls, \
    get_random_method_room_with_wall
from combinations.c03_upper_floor_combinations_lvl_rooms import UpperFloorCombinationsOnlyRooms
from combinations.c04_upper_floor_combinations_lvl_players import UpperFloorCombinationsWithPlayers
from combinations.c05_house_lvl import HouseCombinations
from combinations.utils import get_all_rooms_and_players_from_single_house_comb
from common.constants import MAX_RETRIES
from house.rooms import Room
from new_scenarios.config import MAX_ROOM_OBJ_COMBINATIONS, MAX_ROOM_WALL_COMBINATIONS, \
    MAX_UPPER_FLOOR_ROOM_COMBINATIONS, MAX_UPPER_FLOOR_PLAYER_COMBINATIONS, CHANCE_OF_ALL_ROOM_WALL_COND, \
    CHANCE_OF_ALL_ROOM_OBJ_COND, SET_SEED, SHOW_PRINTS, NR_TRIES, USE_PARALLELIZATION, MAX_HOUSE_COMBINATIONS, \
    MAX_COMBS_TO_CALC
from ui.conditions import split_conds_to_4_players
from ui.pdf_gen import gen_pdf_version

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
    while ((nr_room_combs > MAX_ROOM_OBJ_COMBINATIONS) and (len(all_conds) < 12)):
        if iterations > MAX_RETRIES:
            raise TimeoutError("iteration exceeded MAX_RETRIES")
        iterations += 1
        try:
            rnd_method, method_args = get_random_method_room_obj()
            if random.random() < CHANCE_OF_ALL_ROOM_OBJ_COND:
                method_args["apply_for_all_rooms"] = True
                tmp_conds = []
                fallback_rooms_combs = deepcopy(rooms_combs)
                try:
                    for room in rooms_combs:
                        tmp_conds.append(rnd_method(room, **method_args))
                    current_cond = tmp_conds[0]
                except ValueError as e:
                    rooms_combs = fallback_rooms_combs
                    raise ValueError("One of all_room_obj conditions wasnt possible.")
            else:
                current_room = random.choice(rooms_combs)
                current_cond = rnd_method(current_room, **method_args)
            if SHOW_PRINTS:
                print(current_cond)
            all_conds.append(current_cond)
            room_combs_counter = 1
            for room in rooms_combs:
                room_combs_counter *= len(room.object_combinations)
            nr_room_combs = room_combs_counter
            if SHOW_PRINTS:
                print(nr_room_combs)
        except ValueError as e:
            # print(f"{e}")
            pass

    # Creating wall colors for all rooms
    bedroom1_wall_combs = RoomCombinationsWithWalls(bedroom1_combs.room_name, bedroom1_combs.object_combinations)
    bedroom2_wall_combs = RoomCombinationsWithWalls(bedroom2_combs.room_name, bedroom2_combs.object_combinations)
    livingroom_wall_combs = RoomCombinationsWithWalls(livingroom_combs.room_name, livingroom_combs.object_combinations)
    kitchen_wall_combs = RoomCombinationsWithWalls(kitchen_combs.room_name, kitchen_combs.object_combinations)
    wall_comb_rooms = [bedroom1_wall_combs, bedroom2_wall_combs, livingroom_wall_combs, kitchen_wall_combs]

    # Getting conditions on room (object + wall)
    while ((len(bedroom1_wall_combs) * len(bedroom2_wall_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > MAX_ROOM_WALL_COMBINATIONS) and (len(all_conds) < 12)):
        if iterations > MAX_RETRIES:
            raise TimeoutError("iteration exceeded MAX_RETRIES")
        iterations += 1
        try:
            rnd_method, method_args = get_random_method_room_with_wall()
            if random.random() < CHANCE_OF_ALL_ROOM_WALL_COND:
                method_args["apply_for_all_rooms"] = True
                tmp_conds = []
                fallback_wall_comb_rooms = deepcopy(wall_comb_rooms)
                try:
                    for room in wall_comb_rooms:
                        tmp_conds.append(rnd_method(room, **method_args))
                    current_cond = tmp_conds[len(wall_comb_rooms)-1]
                except ValueError as e:
                    wall_comb_rooms = fallback_wall_comb_rooms
                    raise ValueError("One of all_room_wall conditions wasnt possible.")
            else:
                current_room = random.choice(wall_comb_rooms)
                current_cond = rnd_method(current_room, **method_args)
            all_conds.append(current_cond)
            if SHOW_PRINTS:
                print(current_cond)
                print(len(bedroom1_wall_combs) * len(bedroom2_wall_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))
        except ValueError as e:
            # print(f"{e}")
            pass

    if len(bedroom1_wall_combs.room_wall_combinations) * len(bedroom2_wall_combs.room_wall_combinations) > MAX_COMBS_TO_CALC:
        raise TimeoutError("Too many combs to calc")

    # Creating conditions for upper floor
    upper_floor_combs = UpperFloorCombinationsOnlyRooms(bedroom1_wall_combs.room_wall_combinations, bedroom2_wall_combs.room_wall_combinations)
    while ((len(upper_floor_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > MAX_UPPER_FLOOR_ROOM_COMBINATIONS) and (len(all_conds) < 12)):
        if iterations > MAX_RETRIES:
            raise TimeoutError("iteration exceeded MAX_RETRIES")
        iterations += 1
        try:
            current_cond = upper_floor_combs.get_random_method()
            all_conds.append(current_cond)
            if SHOW_PRINTS:
                print(current_cond)
                print(len(upper_floor_combs))
                print(len(upper_floor_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))

        except ValueError as e:
            # print(f"{e}")
            pass

    if len(upper_floor_combs.upper_floor_combinations_only_rooms) * 6 > MAX_COMBS_TO_CALC:
        raise TimeoutError("Too many combs to calc")
    # Creating player conditions
    upper_floor_player_combs = UpperFloorCombinationsWithPlayers(upper_floor_combs.upper_floor_combinations_only_rooms)
    while ((len(upper_floor_player_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs) > MAX_UPPER_FLOOR_PLAYER_COMBINATIONS) and (len(all_conds) < 12)):
        if iterations > MAX_RETRIES:
            raise TimeoutError("iteration exceeded MAX_RETRIES")
        iterations += 1
        try:
            current_cond = upper_floor_player_combs.get_random_method()
            all_conds.append(current_cond)
            if SHOW_PRINTS:
                print(current_cond)
                print(len(upper_floor_player_combs))
                print(len(upper_floor_player_combs) * len(livingroom_wall_combs) * len(kitchen_wall_combs))

        except ValueError as e:
            pass

    if len(upper_floor_player_combs.upper_floor_combinations_with_players) * \
            len(livingroom_wall_combs.room_wall_combinations) * \
            len(kitchen_wall_combs.room_wall_combinations) > MAX_COMBS_TO_CALC:
        raise TimeoutError("Too many combs to calc")
    # Creating house conditions
    house_combs = HouseCombinations(upper_floor_player_combs.upper_floor_combinations_with_players, livingroom_wall_combs.room_wall_combinations, kitchen_wall_combs.room_wall_combinations)
    while len(all_conds) < 12:
        if iterations > MAX_RETRIES:
            raise TimeoutError("iteration exceeded MAX_RETRIES")
        iterations += 1
        try:
            current_cond = house_combs.get_random_method()
            all_conds.append(current_cond)
            if SHOW_PRINTS:
                print(current_cond)
                print(len(house_combs))

        except ValueError as e:
            pass

    if SHOW_PRINTS:
        print("\n\nAll conditions:\n")
        for cond in all_conds:
            print(cond)

    if len(all_conds) == 12 and len(house_combs) < MAX_HOUSE_COMBINATIONS:
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
    if USE_PARALLELIZATION:
        num_cores = multiprocessing.cpu_count()
        max_workers = min(32, num_cores * 5)
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for idx in range(NR_TRIES):
                futures.append(executor.submit(process_iteration, idx))
            results = []
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
    else:
        for idx in tqdm(range(NR_TRIES)):
            if idx == 5:
                print("")
            process_iteration(idx)
