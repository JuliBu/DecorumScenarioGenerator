def get_rooms_and_players_from_single_upper_floor_combination_with_players(single_upper_floor_combination_with_players):
    bedroom1 = single_upper_floor_combination_with_players[0][0]
    bedroom2 = single_upper_floor_combination_with_players[0][1]
    players_left = single_upper_floor_combination_with_players[1][0]
    players_right = single_upper_floor_combination_with_players[1][1]
    return bedroom1, bedroom2, players_left, players_right


def get_all_rooms_and_players_from_single_house_comb(single_house_comb):
    bedroom1, bedroom2, players_left, players_right = get_rooms_and_players_from_single_upper_floor_combination_with_players(single_house_comb[0])
    livingroom = single_house_comb[1]
    kitchen = single_house_comb[2]
    return bedroom1, bedroom2, players_left, players_right, livingroom, kitchen
