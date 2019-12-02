# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
    def __str__(self):
        return f"Hello {self.name}. Your current location is: {self.currentRoom}"
    
          
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










#========================================
# def moveDir(direction):
     # self.currentRoom=     

# player1 = Player()
# print(player1)