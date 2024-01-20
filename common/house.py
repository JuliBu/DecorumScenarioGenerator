from common.objects import DecorumObject
from common.player import Player
from common.rooms import Room


class House:
    def __init__(self):
        self.bedroom1 = Room("Bedroom1", "blue")
        self.bedroom2 = Room("Bedroom2", "green")
        self.living_room = Room("LivingRoom", "yellow")
        self.kitchen = Room("Kitchen", "red")

    def apply_conditions(self):
        # Condition: Only antique objects on the right
        if self.bedroom2.check_order(["Antique"]):
            print("Condition met: Only antique objects on the right in Bedroom2")
        else:
            print("Condition not met: Only antique objects on the right in Bedroom2")

        # Condition: Only red objects on the left
        if self.kitchen.check_order(["red"]):
            print("Condition met: Only red objects on the left in Kitchen")
        else:
            print("Condition not met: Only red objects on the left in Kitchen")

    def __str__(self):
        return f"House Structure:\n{self.bedroom1}\n{self.bedroom2}\n{self.living_room}\n{self.kitchen}"

# Example usage of the classes
my_house = House()

# Add objects to rooms
my_house.bedroom1.add_object(DecorumObject("Painting", "blue", "Modern"))
my_house.bedroom1.add_object(DecorumObject("Lamp", "red", "Antique"))

my_house.bedroom2.add_object(DecorumObject("Curiosity", "green", "Retro"))
my_house.bedroom2.add_object(DecorumObject("Painting", "yellow", "Antique"))

my_house.living_room.add_object(DecorumObject("Lamp", "green", "Modern"))
my_house.living_room.add_object(DecorumObject("Painting", "red", "Antique"))

my_house.kitchen.add_object(DecorumObject("Curiosity", "red", "Retro"))
my_house.kitchen.add_object(DecorumObject("Lamp", "blue", "Antique"))

# Add players to rooms
my_house.bedroom1.add_player(Player("Alice", "Bedroom1"))
my_house.bedroom1.add_player(Player("Bob", "Bedroom1"))

my_house.bedroom2.add_player(Player("Charlie", "Bedroom2"))
my_house.bedroom2.add_player(Player("David", "Bedroom2"))

# Display house structure and apply conditions
print(my_house)
my_house.apply_conditions()
