from random import randrange

def map_coord(list_coordinates, fruit_position):
    """Maps the list of coordinates in a grid"""
    
    grid1 = []

    for i in range(10):
        grid1.append([])
        for j in range(10):
            grid1[i].append('.')
    
    x_fruit = fruit_position[0][0]
    y_fruit = fruit_position[0][1]
    grid1[x_fruit][y_fruit] = 'F'

    for coordinate in list_coordinates:
        x = coordinate[0]
        y = coordinate[1]
        grid1[x][y] = 'X'

    for i in range(len(grid1)):
        print(grid1[i])


def movement(coordinates,direction, food_position):
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
          status = '!'            #The move touches the snakes's body
        else:
          coordinates.extend(new_point)
          if new_point != food_position:
              coordinates.pop(0)
              status = '-'        # The move did not eat any food
          else:
              status = 'o'        # The move ate a food
            
    return(status)

def add_food(coordinates):
    """Adds food to the grid"""

    food_position = []
    x_food = randrange(0,10)
    y_food = randrange(0,10)
    food_position.append((x_food,y_food))
    while (all(x in coordinates for x in food_position)):
        food_position = []
        x_food = randrange(0,10)
        y_food = randrange(0,10)
        food_position.append((x_food,y_food))
    return(food_position)

def call_moves():
    """Asks user the direction to move"""

    food_position = add_food(test_coordinates)
    map_coord(test_coordinates, food_position)
    move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')

    while move != 'end':
        status = movement(test_coordinates,move, food_position)
        if status == '!':
            move = input("You can't move there. In which direction you want to move? Type 'n', 's', 'e' or 'w', or type 'end' to finish the game. ")
        elif status == '-':
            map_coord(test_coordinates, food_position)
            move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')
        elif status == 'o':
            food_position = add_food(test_coordinates)
            map_coord(test_coordinates, food_position)
            move = input('In which direction you want to move? Type "n", "s", "e" or "w", or type "end" to finish the game. ')

test_coordinates = [(0,0),(0,1),(0,2)]
call_moves()    




