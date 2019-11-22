# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, inventory=[], health=90, mana=95):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = inventory
        self.health = health
        self.mana = mana

    def add_item(self, item):
        self.inventory.append(item)






 # direction method here.
    # def playermove(self, cmd):
    #     if getattr(self.currentRoom, f"{cmd}_to") is not None:
    #         self.currentroom = getattr(self.currentroom, f"{cmd}_to")
    #     else: 
    #         print("nope. You can't go there!")

    # def __str__(self):
    #     output = ''
    #     output += '---------------------------------------- \n'
    #     output += f'Player Name: {self.name} \n'
    #     output += f'Current Room: {self.currentRoom} \n'
    #     return output












#========================================
# def moveDir(direction):
     # self.currentRoom=     

# player1 = Player()
# print(player1)