from common.house import House
from common.rooms import Room


def iter_modifications():
    house = House(Room("bedroom1"), Room("bedroom2"), Room("livingroom"), Room("kitchen"))
    house.bedroom1.filter_items_by_color_and_quantity(3, "red", "min")
    house.bedroom1.filter_items_by_color_and_quantity(2, "red", "max")

if __name__ == '__main__':
    iter_modifications()