
#===============================
#         create matrix
#===============================
def create_matrix(size, fill):
    """this function will create a matrix - default value is 0"""

    #using list comprehension
    return [fill for j in range(size) for i in range(size)]

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
#         render public
#===============================
def render_public():
    pass

#===============================
#         render reveal
#===============================
def render_reveal():
    pass

