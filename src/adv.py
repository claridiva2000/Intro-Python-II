from room import Room
from player import Player
from item import Currency
from item import Weapons 
from item import Food
from room import Monster

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Weapons('A sword called Needle','Stick \'um with the pointy end', 5)],[]), 

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Weapons('A sword called Needle','Stick \'um with the pointy end', 5)],[Monster('jigglypuff','She looks angry!')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def tryDirection(d, currentRoom):
    attrib = d +'_to'

    if hasattr(currentRoom, attrib):
        return getattr(currentRoom, attrib)

    else: 
        print('You can\'t go there')
    
    return currentRoom
#
# Main
#
movement = ['n', 's', 'e', 'w',]

getStarted = input("Welcome to the kingdom of Equestria! \n What is your name? ")
print(f'Nice to meet you, {getStarted}. Let\'s go!!')


# Make a new player object that is currently in the 'outside' room.
player = Player(getStarted, room['outside'])

# Write a loop that:
#

done = False

while not done:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print("\n Current location: {}\n{}".format(player.currentRoom.name, player.currentRoom.description))

    #items in room
    for item in player.currentRoom.items:
        print(item)
    
# * Waits for user input and decides what to do.
#
    s= input("\nCommand> ").strip().lower().split()
# Print an error message if the movement isn't allowed.
#
    if len(s) != 1:
        print("Not sure what you mean. Try again.")
        continue

    # if player.currentRoom.monsters == []:
    #     print('The room looks safe.')
    # else:  
    #     print(f'a wild {player.currentRoom.monsters[0].name} attacks! You strike back with {player.currentRoom.items[0].name}. It\'s super effective!')
    #     continue

# If the user enters "q", quit the game.
    if s[0] == "q" or s[0] == "Q":
        done = True
    
    #     fight= input('Will you (f)ight or (r)un? > ')
    #     if fight == 'f':
    #         print(f'You attack with {player.currentRoom.items[0].name}. It\'s super effective!')
    #     elif fight == 'r':
    #         print('You run away and live to fight another day.')
    #         moveon= input("Continue? (y/n): ")
    #         if moveon == 'y':
    #             continue
    
    
    elif s[0] == 'h':
        print("HELP MENU:\n DIRECTIONS: \n n:north \n s:south \n e:east \n w:west \n q: quit")

# If the user enters a cardinal direction, attempt to move to the room there.
       

    elif s[0] in movement:
        player.currentRoom = tryDirection(s[0], player.currentRoom)    
    else:
        print("unknown command {}. Press 'h' to see the help menu. ".format(' '.join(s)))
    
   
   
