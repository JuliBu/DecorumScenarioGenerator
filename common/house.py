from common.objects import DecorumObject
from common.player import Player
from common.rooms import Room


class House:
    def __init__(self, bedroom1: Room, bedroom2: Room, living_room: Room, kitchen: Room):
        self.bedroom1 = bedroom1
        self.bedroom2 = bedroom2
        self.living_room = living_room
        self.kitchen = kitchen
        self.all_rooms = [bedroom1, bedroom2, living_room, kitchen]


    def __str__(self):
        return f"House Structure:\n{self.bedroom1}\n{self.bedroom2}\n{self.living_room}\n{self.kitchen}"

