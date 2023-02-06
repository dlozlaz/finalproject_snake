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
    new_point = []
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
    if x < 0 or x > 9 or y < 0 or y > 9:
        status = '!'
    else:
        new_point.append((x,y))
        if (all(x in coordinates for x in new_point)):
          status = '!'
        else:
          coordinates.extend(new_point)
          coordinates.pop(0)
          status = '-'
    return(status)

  
def call_moves():
    """Asks user the direction to move"""

    map_coord(test_coordinates)
    move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')

    while move != 'end':
        if movement(test_coordinates,move) == '!':
            move = input("You can't move there. In which direction you want to move? Type 'n', 's', 'e' or 'w', or type 'end' to finish the game. ")
        else:
            map_coord(test_coordinates)
            move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')

test_coordinates = [(0,0),(0,1),(0,2)]
call_moves()    




