import random

# Number of snakes and ladders 
NUM_SNAKES = 8
NUM_LADDERS = 10

# Board size
BOARD_SIZE = 100

# Snakes and ladders dictionary with key as start point and value as end point
snakes = {98: 28, 95: 24, 92: 51, 83: 19, 73: 1, 69: 33, 64: 36, 57: 5}
ladders = {8: 26, 21: 82, 43: 77, 50: 91, 54: 93, 62: 96, 66: 87, 80: 100}

players = []
player_positions = {}

def setup_game():
    num_players = int(input("Enter number of players: "))
    
    for i in range(num_players):
        name = input(f"Enter name for player {i+1}: ")
        players.append(name)
        player_positions[name] = 0
        
def roll_dice():
    return random.randint(1, 6)

def move_player(player, dice_roll):
    old_position = player_positions[player]
    new_position = old_position + dice_roll
    
    if new_position > BOARD_SIZE:
        # Player remains in same position if dice roll takes him beyond board size
        new_position = old_position 
    else:
        for start, end in snakes.items():
            if new_position == start:
                new_position = end
                break # Break to avoid reassigning new_position
        
        for start, end in ladders.items():
            if new_position == start:
                new_position = end
                break
        
    player_positions[player] = new_position
    print(f"{player} rolled a {dice_roll} and moved from {old_position} to {new_position}")
    
def check_winner():
    for player in players:
        if player_positions[player] == BOARD_SIZE:
            print(f"{player} wins!")
            return True
        
    return False
            
def play():
    setup_game()
    while True:
        for player in players: 
            dice_roll = roll_dice()
            move_player(player, dice_roll)
            
            if check_winner():
                break
                
        input("Press enter to continue")
        
play()
