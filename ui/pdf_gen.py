from typing import List

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from common.data_classes import ConditionOutput
from ui.conditions import split_conds_to_4_players


def gen_pdf_version(all_conds: List[ConditionOutput], filename: str, game_ident: str):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 10)
    all_player_conds = split_conds_to_4_players(all_conds)

    first_y = 750
    second_y = 550
    third_y = 350
    fourth_y = 150

    left_x = 100
    right_x = 400

    # Player 1
    c.drawString(left_x, first_y, f"Player 1: {game_ident}")
    for idx, cond in enumerate(all_player_conds[0]):
        c.drawString(left_x, first_y - 25 - idx * 20, f"{idx+1}: {str(cond)}")
    c.line(left_x, first_y - (idx + 2) * 20 - 25, right_x,  first_y - (idx + 2) * 20 - 25)

    # Player 2
    c.drawString(left_x, second_y, f"Player 2: {game_ident}")
    for idx, cond in enumerate(all_player_conds[1]):
        c.drawString(left_x, second_y - 25 - idx * 20, f"{idx+1}: {str(cond)}")
    c.line(left_x, second_y - (idx + 2) * 20 - 25, right_x, second_y - (idx + 2) * 20 - 25)

    # Player 3
    c.drawString(left_x, third_y, f"Player 3: {game_ident}")
    for idx, cond in enumerate(all_player_conds[2]):
        c.drawString(left_x, third_y - 25 - idx * 20, f"{idx+1}: {str(cond)}")
    c.line(left_x, third_y - (idx + 2) * 20 - 25, right_x, third_y - (idx + 2) * 20 - 25)

    # Player 4
    c.drawString(left_x, fourth_y, f"Player 4: {game_ident}")
    for idx, cond in enumerate(all_player_conds[3]):
        c.drawString(left_x, fourth_y - 25 - idx * 20, f"{idx+1}: {str(cond)}")

    c.showPage()
    c.save()
