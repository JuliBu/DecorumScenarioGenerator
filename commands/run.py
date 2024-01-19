from common.objects import DecorumObject
from common.rooms import Room

kueche = Room("Küche", "rot")
schlafzimmer1 = Room("Schlafzimmer1", "blau")

try:
    obj1 = DecorumObject("Kuriosität", "rot", "Modern")
    kueche.add_object(obj1)

    obj2 = DecorumObject("Bild", "grün", "Antik")
    schlafzimmer1.add_object(obj2)

    obj3 = DecorumObject("Lampe", "blau", "Retro")
    kueche.add_object(obj3)

    # Beispiel für die Verwendung von check_order
    expected_order = ["Kuriosität", "Bild", "Lampe"]
    if kueche.check_order(expected_order):
        print(f"Die Objekt-Reihenfolge in der {kueche.name} ist korrekt.")
    else:
        print(f"Die Objekt-Reihenfolge in der {kueche.name} ist nicht korrekt.")

    print(kueche)
    print(schlafzimmer1)
except ValueError as e:
    print(e)
