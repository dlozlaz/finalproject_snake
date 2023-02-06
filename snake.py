def map_coord(list_coordinates):
    """Maps the list of coordinates in a grid"""
    
    grid1 = []

    for i in range(10):
        grid1.append([])
        for j in range(10):
            grid1[i].append('.')

    for coordinate in list_coordinates:
        x = coordinate[0]
        y = coordinate[1]
        grid1[x][y] = 'X'

    for i in range(len(grid1)):
        print(grid1[i])


def movement(coordinates,direction):
    """Moves list in a given direction"""
    x = coordinates[-1][0]
    y = coordinates[-1][1]
    if direction == 'e':
        y = y + 1
    elif direction == 'w':
        y = y - 1
    elif direction == 's':
        x = x + 1
    elif direction == 'n':
        x = x - 1
    coordinates.append([x,y])

  
def call_moves():
    """Asks user the direction to move"""

    map_coord(test_coordinates)
    move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')
    while move != 'end':
        movement(test_coordinates,move)
        map_coord(test_coordinates)
        move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')

test_coordinates = [(0,0),(0,1),(0,2)]
call_moves()    




