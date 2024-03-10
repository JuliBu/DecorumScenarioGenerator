from typing import Optional

from new_scenarios.config import USED_LANGUAGE


class ConditionOutput:
    def __init__(self, eng_output: str, ger_output: str, specific_player: Optional[int] = None):
        self.english_cond = eng_output
        self.german_cond = ger_output
        self.specific_player = specific_player

    def __str__(self):
        if USED_LANGUAGE == "german":
            out_str = self.german_cond
        elif USED_LANGUAGE == "english":
            out_str = self.english_cond
        else:
            raise NotImplementedError

        if self.specific_player is not None:
            out_str = f"Specific_player: {self.specific_player}, " + out_str

        return out_str
