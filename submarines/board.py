#===============================
#         create matrix
#===============================
def create_matrix(size, fill):
    """this function will create a matrix - default value is 0"""

    #using list comprehension
    return [[fill for j in range(size)] for i in range(size)]

#===============================
#           in bounds
#===============================
def in_bounds(n, x, y):
     return 0 < x < n and 0 < y < n

#===============================
#     count remaining ships
#===============================
def count_remaining_ships(ships, shots):

    count = 0

    for i in range(len(ships)):
        for j in range(len(ships[i])):
            if ships[i][j] == 1 and shots[i][j] == False:
                count += 1

    return count


#===============================
#         get character
#===============================
def get_character(ships, shots, row, col):

    if shots[row][col] and ships[row][col] == 0:
        return 'X'
    elif shots[row][col] and ships[row][col] == 1:
        return 'V'
    elif not shots[row][col]:
        return 'O'

#===============================
#         render public
#===============================
def render_public(ships, shots):

    return_string = ""

    for row in range(len(ships)):
        for col in range(len(ships)):
             character = get_character(ships, shots, row, col)
             return_string += f"{character} "

        return_string += '\n'

    return return_string

#===============================
#         render reveal
#===============================
def render_reveal():
    pass

