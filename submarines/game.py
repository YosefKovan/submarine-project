from submarines.board import create_matrix, in_bounds, render_public
from submarines.placement import place_random_ships

#==============================
#     handle_successful_shot
#==============================
def handle_successful_shot(game_data, row, col):

    game_data["shots"][row][col] = True

    if game_data["ships"][row][col] == 1:
        return True, "Shot Hit The Ship"
    else:
        return True, "Shot Missed The Ship"

#==============================
#           shoot
#==============================
def shoot(game_data, row, col):

    if game_data["max_shots"] - game_data["shots_used"] <= 0:
        return False, "You do not have any bullets left"

    if not in_bounds(len(game_data["ships"]), row, col):
        return False, "The coordinates tou gave are out of bounds!"

    if game_data["shots"][row][col]:
       return False, "You have shot already in that spot please try again!"

    #this will return the result of the successful hit (did it hit a ship or not)
    return handle_successful_shot(game_data, row, col)

#==============================
#         player won
#==============================
def player_won(game_data):
    return remaining_ships(game_data) == 0 and shots_left(game_data) > 0

#==============================
#         player lost
#==============================
def player_lost(game_data):
    return remaining_ships(game_data) > 0 and shots_left(game_data) == 0

#==============================
#         shots left
#==============================
def shots_left(game_data):
    return game_data["max_shots"] - game_data["shots_used"]

#==============================
#       remaining ships
#==============================
def remaining_ships(game_data):
    """return the amount of ships remaining on the board"""
    count_remaining_ships = 0

    for row in range(game_data["size"]):
       for col in range(game_data["size"]):
           if game_data["ships"][row][col] == 1 and not game_data["shots"][row][col]:
               count_remaining_ships += 1

    return count_remaining_ships

#==============================
#          init_game
#==============================
def init_game(size, ships, max_shots):

    ship_matrix = create_matrix(size, 0)
    place_random_ships(ship_matrix, ships)

    game_data = {
        "size" : size,
        "ships" : ship_matrix,
        "shots" : create_matrix(size, False),
        "n_ships" : ships,
        "max_shots" : max_shots
    }

    return game_data

#==============================
#         play game
#==============================
def play_game(size, ships, max_shots, amount_of_ships):

    game_data = init_game(size, ships, max_shots, amount_of_ships)

    while not player_won(game_data) or player_lost(game_data):
        render_public(game_data["ships"], game_data["shots"])






