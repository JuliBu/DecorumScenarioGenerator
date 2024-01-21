
OBJ_COLORS = ["red", "green", "yellow", "blue"]
AVAILABLE_ROOMS = ["bedroom1", "bedroom2", "livingroom", "kitchen"]
POSITIONS = ["left", "middle", "right"]
OBJ_TYPES = ["curiosity", "painting", "lamp"]
STYLES = ["modern", "antique", "retro", "rare"]

ALLOWED_CURIOSITIES = [
    ("curiosity", "green", "modern"),
    ("curiosity", "blue", "antique"),
    ("curiosity", "yellow", "retro"),
    ("curiosity", "red", "rare"),
]
ALLOWED_PAINTINGS = [
    ("painting", "red", "modern"),
    ("painting", "green", "antique"),
    ("painting", "blue", "retro"),
    ("painting", "yellow", "rare"),
]
ALLOWED_LAMPS = [
    ("lamp", "blue", "modern"),
    ("lamp", "yellow", "antique"),
    ("lamp", "red", "retro"),
    ("lamp", "green", "rare"),
]
ALLOWED_COMBINATIONS = ALLOWED_CURIOSITIES + ALLOWED_PAINTINGS + ALLOWED_LAMPS
