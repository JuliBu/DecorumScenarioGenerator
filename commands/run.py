# Example usage of the classes
from common.objects import DecorumObject
from common.player import Player
from common.rooms import Room

kitchen = Room("Kitchen", "red")
bedroom1 = Room("Bedroom1", "blue")
bedroom2 = Room("Bedroom2", "green")

try:
    obj1 = DecorumObject("Curiosity", "red", "Modern")
    kitchen.add_object(obj1)

    obj2 = DecorumObject("Painting", "green", "Antique")
    bedroom1.add_object(obj2)

    obj3 = DecorumObject("Lamp", "blue", "Retro")
    kitchen.add_object(obj3)

    player1 = Player("Alice", "Bedroom1")
    player2 = Player("Bob", "Bedroom1")

    # Try adding more than 2 players to Bedroom1 (will raise ValueError)
    player3 = Player("Charlie", "Bedroom1")
    bedroom1.add_player(player1)
    bedroom1.add_player(player2)
    bedroom1.add_player(player3)

    # Example usage of check_order
    expected_order = ["Curiosity", "Painting", "Lamp"]
    if kitchen.check_order(expected_order):
        print(f"The object order in the {kitchen.name} is correct.")
    else:
        print(f"The object order in the {kitchen.name} is not correct.")

    print(kitchen)
    print(bedroom1)
except ValueError as e:
    print(e)