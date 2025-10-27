from submarines.game import shots_left, remaining_ships
from submarines.board import render_public

#================================
#       player_input_func
#================================
def player_input_func():

    valid_input = False

    while not valid_input:

        player_input = input("Please enter a row and a col: ")
        player_input = player_input.split(" ")

        if len(player_input) == 2 and player_input[0].isdigit() and player_input[0].isdigit():
            return player_input[0], player_input[1]


#================================
#         print status
#================================
def print_status(game_data):
    print("Bullets left: " + shots_left(game_data))
    print("Ships Left: " + remaining_ships(game_data))
    print(render_public(game_data["ships"], game_data["shots"]))


#================================
#           print end
#================================
def print_end(game_data, won):

    if won:
        print("You won congrats!")
    else:
        pass
