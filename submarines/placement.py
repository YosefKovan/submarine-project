from random import randrange

#================================
#        get_random_cell
#================================
def get_random_cell(min_cell, max_cell):
    """this function will return a random row and col"""
    row = randrange(min_cell, max_cell)
    col = randrange(min_cell, max_cell)

    return row, col

#================================
#       place_random_ships
#================================
def place_random_ships(ships, amount_of_ships):
    """this function will place the ships randomly"""

    while amount_of_ships > 0:
        row, col = get_random_cell(min, max)
        ships[row][col] = 1

