class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'
    
    def __repr__(self):
        return f'Item({repr(self.name)}: {repr(self.description)})'
    

# class Food(Item):
#     def __init__(self, name, description, addHealth)
#         super().__init__(name, description)
#         self.addHealth = addHealth


# class Currency(Item):
#     def __init__(self, name, description, value):
#         super().__init__(name, description)
#         self.value = value

    