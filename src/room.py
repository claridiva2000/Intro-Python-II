# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
     


    def __str__(self):
        output = ''
        output += f"{self.name}"
        output += f"{self.description}"
        output += f'{self.items}'
        return output