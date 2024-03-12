from typing import List

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from common.data_classes import ConditionOutput
from ui.conditions import split_conds_to_4_players


def gen_pdf_version(all_conds: List[ConditionOutput], filename: str, game_ident: str, nr_house_combs: int, language: str):
    c = canvas.Canvas(filename, pagesize=(letter[1], letter[0]))
    c.setFont("Helvetica", 10)
    all_player_conds = split_conds_to_4_players(all_conds)

    info_y = 550
    first_y = 420
    second_y = 320
    third_y = 220
    fourth_y = 120

    row_distance = 20

    left_x = 30
    right_x = 600

    # Scenario info
    c.drawString(left_x, info_y, f"Game_ID: {game_ident}, Nr of possible house combs: {nr_house_combs}")
    c.line(left_x, info_y-30, right_x, info_y-30)

    # Player information
    players_info = [
        {"y": first_y, "text": "Player 1"},
        {"y": second_y, "text": "Player 2"},
        {"y": third_y, "text": "Player 3"},
        {"y": fourth_y, "text": "Player 4"}
    ]

    for player_info, player_conds in zip(players_info, all_player_conds):
        c.drawString(left_x, player_info["y"], f"{player_info['text']}: {game_ident}")
        for idx, cond in enumerate(player_conds):
            if language == "ger":
                text = cond.german_cond
            elif language == 'eng':
                text = cond.english_cond
            else:
                raise NotImplementedError
            c.drawString(left_x, player_info["y"] - 25 - idx * row_distance, f"{idx+1}: {text}")
        c.line(left_x, player_info["y"] - (idx + 1) * row_distance - 20, right_x, player_info["y"] - (idx + 1) * row_distance - 20)

    c.showPage()
    c.save()
