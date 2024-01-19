class Player:
    def __init__(self, name, bedroom):
        self.name = name
        self.bedroom = bedroom

    def __str__(self):
        return f"{self.name} in {self.bedroom} bedroom"