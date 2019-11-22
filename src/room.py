# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], monsters=[]):
        self.name = name
        self.description = description
        self.items = items
        self.monsters = monsters
     


class Monster(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        

    # def __str__(self):
    #   return f'you found {self.name}: \n hit points: {self.hitPoints} \n description: {self.description}'



