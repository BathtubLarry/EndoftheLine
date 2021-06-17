# Dustin Runkel

# hey Dr. Mike! I tried to make this code as scalable as I could. This code should be able to take as many items
# as one could want, and adding rooms is easy. Hopefully I can clean it up and turn it into a nice portfolio piece.
# I would like to take multiple arguments for picking up items because I think the menu system is kind of clunky
# I hope you have as much fun playing as I did creating this!

# for this section i made room into a class and defined a bunch of things about the rooms I wanted to store to
# a particular room
class Room:

    def __init__(self, name, desc, move_to=['Hallway'], current='False'):
        self.name = name
        self.desc = desc
        # the first two are self explanatory
        # move_to contains a list of the rooms available to move to
        self.move_to = move_to
        # current evaluates to true when the player is in that room
        self.current = current

    def examine(self):
        print(self.desc)

# defining the non - default values of the rooms


fred_cell = Room(
    'Fred\'s Cell',
    'Old food wrappers litter the floor, that\'s the way fred always keeps it.\n Unreturned books'
    'from the library are hidden amongst ramen cups and candy wrappers.\n Why did Fred\'s doctor never made him '
    'clean it... '
)

my_cell = Room(
    'My Cell',
    'Blood is all over the ripped apart books, my Alex Grey poster \'Dying\' is perfectly intact hanging on the wall. '
    'Must have been one of those psychosomatic reactions the doctor was talking about.\n Or was someone in here? '
    'Did that rat bastard Ricky do this?\nWhatever,I\'ll clean this up later.... Why was my door left open...? ',
    current='True'
)

ricky_cell = Room(
    'Ricky\'s Cell',
    'Manga is neatly lined on a self over his bed,his bed is a mess as if he just woke up. His anime \n body pillow '
    'still tucked in. Seems to be nothing out of the ordinary here. '
)

morgue = Room(
    'Morgue',
    'A small dark room that has a faint glow. In the darkness you see a body covered in a white sheet,\n with a toe'
    'tag hanging off its foot. That\'s weird... I didn\'t hear of any deaths recently. ',
)

showers = Room(
    'Showers',
    'A large open room with shower heads on the wall. Streaks of dirt run along the floor and into the \ndrain. Benches'
    'and foot lockers accompany one side of the room. '
)

mess_hall = Room(
    'Mess Hall',
    'A long bench table lies in the center of the room. At one end is a roll-up window that is shut\n tight where the'
    'food is served from. Place smells like greasy food. '
)

library = Room(
    'Library',
    'A room with dingy blue carpet and books strewn everywhere. The steel rolling-cart tan bookshelves have\n'
    'been pushed around the room, as if someone had been looking for something. '
)

hallway = Room(
    'Hallway',
    'A long narrow room with 3 doors on each side. The walls are of white tile that look like they haven\'t\n '
    'been cleaned in a while. ',
    [fred_cell.name, my_cell.name, ricky_cell.name, morgue.name, showers.name, mess_hall.name, library.name]
    )

# I included a list of rooms here for easy reference in functions

room_list = [fred_cell, my_cell, ricky_cell, morgue, showers, mess_hall, library, hallway]


class Item:                         # this class defines all I want to know about an item

    def __init__(self, name, desc, room, picked_desc, picked='False'):
        self.name = name
        self.desc = desc
        # name and description of the item
        self.room = room
        # room defines the room the item is in
        self.picked = picked
        # picked returns true if the player picked up that item
        self.picked_desc = picked_desc
        # picked desc includes a string added to the room examination while an item is in the room.


book_cover = Item(
    'Book Cover',
    'Torn book cover of \'Lord of the Flies\'',
    library,
    'A torn cover of a book is lying on the ground in the center of the aisle.'
)

newspaper = Item(
    'Newspaper',
    'It\'s today\'s obituary. My name is on it.... Or some other unlucky sap with the same name.',
    fred_cell,
    'The last page of the local newspaper remains on the table as if fred has just read it himself.'
)

note = Item(
    'Note',
    'It\'s a note telling the staff to no longer deliver my food... Do they plan to starve me?',
    hallway,
    'On the door next to my room hangs a note.'
)

menu = Item(
    'Menu',
    'Last weeks menu... I don\'t remember having cake yesterday though...',
    mess_hall,
    'A lone menu sits under the bench of the table.'
)

manga = Item(
    'Berserk Manga',
    'A manga that contains a story of betrayal, but most importantly about struggle and suffering.',
    ricky_cell,
    'Except one of his Berserk Manga is out of order...'
)

picture = Item(
    'Picture',
    'A picture from chess night dated from last night... everyone looks sad and I\'m not there. I must have been '
    'locked in my cell.',
    showers,
    'On Ricky\'s footlocker I can see a photo that wasn\'t there yesterday. Where is everyone...'
)
body = Item(
    'Body',
    'null',
    morgue,
    'null',
)


item_list = [book_cover, newspaper, note, menu, manga, picture, body]


def start():
    a = """

 _______  _        ______     _______  _______   _________          _______    _       _________ _        _______ 
(  ____ \( (    /|(  __  \   (  ___  )(  ____ \  \__   __/|\     /|(  ____ \  ( \      \__   __/( (    /|(  ____  |
| (    \/|  \  ( || (  \  )  | (   ) || (    \/     ) (   | )   ( || (    \/  | (         ) (   |  \  ( || (    \/
| (__    |   \ | || |   ) |  | |   | || (__         | |   | (___) || (__      | |         | |   |   \ | || (__    
|  __)   | (\ \) || |   | |  | |   | ||  __)        | |   |  ___  ||  __)     | |         | |   | (\ \) ||  __)   
| (      | | \   || |   ) |  | |   | || (           | |   | (   ) || (        | |         | |   | | \   || (      
| (____/\| )  \  || (__/  )  | (___) || )           | |   | )   ( || (____/\  | (____/\___) (___| )  \  || (____/ |
(_______/|/    )_)(______/   (_______)|/            )_(   |/     \|(_______/  (_______/\_______/|/    )_)(_______/
                                                                                                                  
████████▓▓██▓▓▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒░░██░░░░░░░░░░██________░░██░░░░░░░░░░██░░▒▒▒▒▒▒▒▒██▒▒▓▓▓▓▓▓██
██████▓▓▓▓██▓▓▓▓▓▓▒▒▒▒██▒▒▒▒▒▒░░░░██░░░░______██__________██░░░░░░░░░░██░░▒▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓
████▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒██▒▒▒▒░░░░░░██░░________██__________██░░░░░░░░░░██░░▒▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓
████▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒██▒▒░░░░░░░░██__________██__________██░░░░████████░░▒▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓
██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██__________██__________██░░░░██████████▒▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓
██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░__██__________██________░░██░░░░████████████▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓
██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░__██__________██______░░▒▒██▒▒▒▒████████████████████▒▒▒▒▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒░░██░░░░░░░░__██__________██____░░░░████████████████████████████████▓▓▓▓▓▓
██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒░░██░░░░░░░░__██__________██__░░░░░░▒▒████████████████████████████████▓▓▓▓
▓▓▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒░░██░░░░░░░░░░██__________██░░░░░░░░░░██████████████████████████████████▓▓
██▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒░░██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██░░██████▒▒████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████
▓▓▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒░░██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██░░░░██████████████████████████████
██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██░░▒▒██████████████████████████████
██████████████████████████▓▓▓▓██▓▓██▓▓▓▓██▓▓██████████████████████████████████████████████████
▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██░░░░░░░░░░██░░░░░░▒▒▒▒██▒▒▒▒████████████▓▓████████████████
▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░░░██░░░░░░░░░░██░░▒▒▒▒▒▒▒▒██▒▒▒▒██████████▒▒▓▓▓▓██████████████
▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▓▓██████████████████████████████
████▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒████████████████████████████████
████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒████████████████████████████████
██████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▓▓████████████████████████████████
████████▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▓▓██▓▓████████████████████████████████
████████████▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓██████████▓▓████████████████████
██████████████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓████████████████████████████████
████████████▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▒▒▓▓▒▒▒▒▒▒██▒▒▒▒▓▓▒▒▓▓██▓▓██████████▓▓▓▓██████████████████
██████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒██████▓▓██▓▓▓▓██████████████████
████▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒██▒▒▒▒▒▒▒▒░░██░░░░░░░░░░██░░░░░░░░▒▒██████████▒▒██▒▒▒▒██████████████████
██▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒██▒▒░░░░░░░░██░░░░░░░░░░██░░░░░░░░░░██████████▒▒██▒▒▒▒██████████████████
████▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒██▒▒░░░░░░░░██__________██____░░░░░░████████▒▒▒▒██▒▒▒▒██████████████████
██████▓▓▓▓██▓▓▓▓▒▒▒▒▒▒██▒▒▒▒░░░░░░██░░░░░░░░__██░░░░░░░░░░████████▒▒▒▒██▒▒▒▒██████████████████
████████████▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░██░░░░░░▒▒████████████▒▒██▒▒▒▒██████████████████
██████████████████████████▓▓██▓▓▓▓██▓▓██▓▓▓▓▓▓██▓▓████████████████████████████████████████████
████████████████████████▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒██▒▒████████████████▓▓▓▓██▓▓▓▓██████████████████
"""
    print(a)
    print('A project by Dustin Runkel')
    start_game = input('press (y) to begin (n) to exit.')
    if start_game == 'y':
        return
    else:
        quit()


# This function takes the list of room objects and updates the current room to the user specified room

def room_movement(room):
    # ask for movement

    print('What room would you like to move to?')

    # check current room

    cur_room = current_room(room)

    # print available rooms

    print(*cur_room.move_to, sep=', ')

    # get user input

    tmp = input().lower()

    # check if user input is valid by checking the input against the container variable for valid rooms to
    # move to

    lower_list = []            # this converts the user input to lowercase and checks it against appropriate values
    for x in cur_room.move_to:
        lower_list.append(x.lower())  # this loop converts room names to lowercase

    if tmp in lower_list:

        # iterate over room list to set the user defined room as TRUE
        # and set others to FALSE

        for x in room:
            if tmp == x.name.lower():
                x.current = 'True'
            else:
                x.current = 'False'
    else:
        print('Invalid Input -- Please type in a valid room name.')
        return

    print('I move from {} to {}'.format(cur_room.name, tmp.capitalize()))  # TODO

# This function takes room list and items, checks if an item is in the current room,
# and returns an updated container indicating the item has been picked up.


def pick_up(rooms, items):
    # iterate over the item list
    for item in items:
        if current_room(rooms) == item.room and item.picked == 'False':  # check current room and if item in inv

            # ask for user input on which item they want to pick up (based on txt in the description of room)

            tmp = input('What item would you like to pick up?:\n').lower()

            # check if the user input is valid

            if tmp == item.name.lower():

                # if user input is valid then update the item and print confirmation to user

                print('You pick up the {}'.format(item.name))

                item.picked = 'True'

                # return the item so its status can be updated

                return item

            else:

                # if the user inputs invalid item name

                print('You can\'t pick that up')

                return
        elif current_room(rooms) == item.room and item.picked == 'True':

            # if the user already picked up the item in the room this statement prints

            print('You have already picked up the item(s) in this room')
            return

    # this statement only prints if there are no items in the room.
    print('You can\'t pick up any items in this room.')


def cmd_help():
    a = """
move - Type 'move' to enter room move menu.
pick up - Type 'pick up' to enter the item pick up menu. 
examine - Type 'examine' to get a description on the room or object.
Be sure to lower your insanity level to 0 before attempting to win the game.
Please note - you must type in the action again after an unexpected input. 

For example - you type in 'move' and the computer will ask where to move to.
In some cases,a list will of valid commands be printed in order to assist you. 
But of course, I can't make it too easy ;)
    """
    print(a)


def opening():
    a = '''
You wake up in your cell at the Collinsworth insanitorium. You are curious as to why the door to your tiny cell has 
been left open. Scattered around you are torn papers, presumably pages from a book. You get up out of your bunk and
in the soft glow of the light you can see blood everywhere, your stomach twists as something doesn't 
feel right.

For a list of commands, type 'help'.   
    '''
    print(a)
    print('Insanity level: 100')


def current_room(room):
    for x in room:
        if x.current == 'True':
            return x


def ins_lvl(items):
    # this loop counts the number of items and calculates the insanity level of the player
    i = 0
    for item in items:
        if item.picked == 'True':
            i -= 1                  # i is negative here to take this value from the base level of 100
        else:
            continue
    tmp = i/(len(items) - 1)             # tmp negative (-1 to remove 'body from this calculation)
    return int((tmp * 100) + 100)       # returns positive percentage amount of insanity


def examine(items, rooms, ins):
    # ask user for item they want to examine
    tmp = input('What would you like to examine?\n').lower()

    # this loop iterates through all the items
    if tmp == body.name.lower() and current_room(rooms) == morgue:
        body.picked = 'True'
        game_check(items, ins)


    for item in items:

        # checking if the input matches any items in inv, or current room

        if tmp == item.name.lower() and (item.room == current_room(rooms) or item.picked == 'True'):

            # stops loop and prints the description if item found

            print(item.desc)

            return

    for room in rooms:           # iterating through the items / rooms to print the combined description if an item
                                # is still in the room
        for item in items:

            if tmp in room.name.lower() and item.picked == 'True':  # prints regular description
                print(room.desc)
                return
            elif tmp in room.name.lower() and item.picked == 'False': # prints description if item is still in room
                print(room.desc + item.picked_desc)
                return

    # these let the player examine their own inventory or insanity level

    if tmp == 'inv' or tmp == 'inventory':

        for item in item_list:

            if item.picked == 'True':

                print(item.name)
        return

    elif tmp == 'level' or tmp == 'insanity level':

        print('Insanity level: {}'.format(ins_lvl(item_list)))

        return

    # error message if the input falls through all the loops
    print('Please enter a valid item to examine -- for help type \'help\'')


def game_check(ins):

    if ins == 0 and body.picked == 'True':
        a = """
I feel warm..., comfortable, more than I ever have. This vessel of flesh was mine own. 
My inhibitions slip from the clear pool of focus and to the bottom of the ocean of the
collective, my human emotions and tact melt from my focus. My human burden of consciousness
is no longer on my shoulders. The lifeless face of my body, which brought so many others joy, love, and happiness,
finally... finally brings me peace.     
    
You win the game!

    """
        print(a)
        exit()

    elif ins != 0 and body.picked == 'True':
            b = ("\n"
                 "I go black. I am consumed with feelings of rage, pain and suffering. It can't be. Please...\n"
                 "\n"
                 "You lose. \n"
                 "\n")
            print(b)
            exit()
    else:
        return


game_state = 'False'

# Gameplay loop

start()

opening()

insanity_level = ins_lvl(item_list)

# each input, the win condition is checked, if it is not met, the user must keep entering commands until it is
while game_state == 'False':
    # global user command

    user_cmd = input().lower().strip()

    # this part checks the user input for certain commands and executes accordingly

    if user_cmd == 'help':

        cmd_help()

    elif user_cmd == 'move':

        room_movement(room_list)

    elif user_cmd == 'pick up':

        pick_up(room_list, item_list)

    elif user_cmd == 'examine':

        examine(item_list, room_list, insanity_level)

    else:

        print('Please type in a valid input. Type (help) for commands.')
