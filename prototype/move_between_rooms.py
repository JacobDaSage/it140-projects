"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


current_room = "Great Hall"
while current_room != "exit":
    print("You are in the", current_room)
    command = input("Enter your command: ").Lower().strip()
if command == "exit":
     current_room = "exit"
    print("Thanks for playing!")
elif command.startswith("go "):
    direction = command[3:}
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("You cannot go that way!")
else:
    print(:Invalid command. Please tryagian.")
    
