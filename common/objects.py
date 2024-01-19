


class DecorumObject:
    allowed_combinations = [
        ("Painting", "red", "Modern"),
        ("Painting", "green", "Antique"),
        ("Painting", "blue", "Retro"),
        ("Painting", "yellow", "Selten"),

        ("Curiosity", "green", "Modern"),
        ("Curiosity", "blue", "Antique"),
        ("Curiosity", "yellow", "Retro"),
        ("Curiosity", "red", "Selten"),

        ("Lamp", "blue", "Modern"),
        ("Lamp", "yellow", "Antique"),
        ("Lamp", "red", "Retro"),
        ("Lamp", "green", "Selten"),
    ]
    def __init__(self, obj_type, color, style):
        self.obj_type = obj_type
        self.color = color
        self.style = style
        if (self.obj_type, self.color, self.style) not in self.allowed_combinations:
            raise ValueError("Ungültige Kombination für DecorumObject")

    def __str__(self):
        return f"{self.color} {self.style} {self.obj_type}"

# Beispiel für die Verwendung der Klasse
obj1 = DecorumObject("Painting", "red", "Antique")
print(obj1)
