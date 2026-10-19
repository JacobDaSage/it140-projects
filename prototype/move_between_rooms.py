# Module Six Milestone: Moving Between Rooms

# Dictionary containing the rooms and their connections
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

# Set the player's starting room
current_room = 'Great Hall'

# Continue playing until the player exits
while current_room != 'exit':
    print('\nYou are in the', current_room)
    print('Available commands: go north, go south, go east, go west, exit')

    command = input('Enter your command: ').lower().strip()

    if command == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')

    elif command.startswith('go '):
        direction = command[3:]

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print('You cannot go that way!')

    else:
        print('Invalid command. Please try again.')
