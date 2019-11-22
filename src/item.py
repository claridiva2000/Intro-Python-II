class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name}: {self.description}'
    

class Food(Item):
    def __init__(self, name, description, addHealth):
        super().__init__(name, description)
        self.addHealth = addHealth


class Currency(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value


class Weapons(Item):
    def __init__(self, name, description, hitPoints):
        super().__init__(name, description)
        self.hitPoints = hitPoints

    def __str__(self):
      return f'you found {self.name}: \n hit points: {self.hitPoints} \n description: {self.description}'


# gold = Currency('gold', 'cha-ching!', 100)