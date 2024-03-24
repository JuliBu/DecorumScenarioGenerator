from typing import List

from fpdf import FPDF

from common.data_classes import ConditionOutput
from ui.conditions import split_conds_to_4_players


def gen_pdf_version(
    all_conds: List[ConditionOutput],
    filename: str,
    game_ident: str,
    nr_house_combs: int,
    language: str,
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    all_player_conds = split_conds_to_4_players(all_conds)

    # Calculate box dimensions
    page_width = 210
    page_height = 297
    margin = 0  # Space around the boxes
    padding = 7  # Space inside boxes
    box_width = (page_width - 3 * margin) / 2
    box_height = (page_height - 3 * margin) / 2
    y_offset = 10

    # Write meta information about the game at the top
    pdf.set_xy(0, 0)
    pdf.cell(
        0,
        10,
        f"Game_ID: {game_ident}, Nr of possible house combs: {nr_house_combs}",
        ln=True,
    )

    # Loop to create 4 boxes, i.e. print information for each player
    for row in range(2):
        for col in range(2):
            x = margin + col * (box_width + margin)
            y = margin + row * (box_height + margin) + y_offset

            # Draw box border
            pdf.rect(x, y, box_width, box_height)

            # Add title "Player x"
            player_idx = row * 2 + col + 1
            player_title = f"Player {player_idx}: {game_ident}"
            pdf.set_xy(x + padding, y + padding)
            pdf.cell(0, 10, player_title, ln=True)

            # Gather conditions as list
            player_conds = all_player_conds[player_idx - 1]
            enumeration = []
            for i, cond in enumerate(player_conds):
                if language == "ger":
                    enumeration.append(f"{cond.german_cond}")
                elif language == "eng":
                    enumeration.append(f"{cond.english_cond}")
                else:
                    raise NotImplementedError

            # Add enumeration with long test strings
            # enumeration = [
            #     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            #     "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            #     "For room livingroom, it applies: If at least 1 object has obj_type = lamp, then there must also be an object with style = retro.",
            # ]

            # Print each condition as enumeration item
            initial_x = x + padding
            pdf.set_xy(initial_x, y + 20)
            cell_width = box_width - padding * 2  # Adjusted width for wrapping
            for i, item in enumerate(enumeration, start=1):
                pdf.multi_cell(cell_width, 7, f"{i}. {item}")
                # Reset x coordinate for subsequent items to match indentation
                pdf.set_xy(initial_x, pdf.get_y() + 5)

    pdf.output(filename)
