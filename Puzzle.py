import queue
import copy

def solve_puzzle(Board, Source, Destination):
    # For coordinate tuples, the left value is the row index and the right value is the column index. I.e. (0,1) means row 1 and column 2
    # The queue will contain tuples with a coordinate and it's previous coordinate
    q = queue.Queue()
    rowCount = len(Board)
    colCount = len(Board[0])

    # Making deep copy of board adapted from Hao Rong's comment in the following Ed discussion: https://edstem.org/us/courses/13739/discussion/867740
    boardCopy = copy.deepcopy(Board)

    # print(boardCopy)

    # The queue determines the order of coordinates to traverse and facilitates a breadth-first search for the graph traversal algorithm.
    q.put((Source, Source))

    
    while not q.empty():
        # Retrieve next coordinate tuple available in the queue
        current = q.get()
        row = current[0][0]
        column = current[0][1]

        # Initialize the coordinate on the board copy with the previously traversed coordinate
        boardCopy[row][column] = current[1]

        # If the space in a direction has not traversed(and is not a wall or obstacle) and the destination coordinate 
        # is empty space that has not been traversed yet(the space is traversed if initialized with the coordinate of a previously traversed space
        # on a path i.e. "(2,0)"), then add a tuple of the coordinate of that space and the coordinate of the current space to the queue. 
        if column - 1 >= 0 and boardCopy[row][column - 1] != '#' and boardCopy[row][column - 1] == '-' and boardCopy[Destination[0]][Destination[1]] == '-':
            coordinate = (row, column - 1)
            q.put((coordinate, current[0]))
        if row - 1 >= 0 and boardCopy[row - 1][column] != '#' and boardCopy[row - 1][column] == '-' and boardCopy[Destination[0]][Destination[1]] == '-':
            coordinate = (row - 1, column)
            q.put((coordinate, current[0]))
        if column + 1 < colCount and boardCopy[row][column + 1] != '#' and boardCopy[row][column + 1] == '-' and boardCopy[Destination[0]][Destination[1]] == '-':
            coordinate = (row, column+1)
            q.put((coordinate, current[0]))
        if row + 1 < rowCount and boardCopy[row + 1][column] != '#' and boardCopy[row + 1][column] == '-' and boardCopy[Destination[0]][Destination[1]] == '-':
            coordinate = (row+1, column)
            q.put((coordinate, current[0]))

    # Begin the making a list of coordinates forming the shortest path from the source to the destination 
    list = []

    # Initialize "current" variable with tuple containing destination coordinate 
    # and the previously traversed coordinate of the destination coordinate
    current = (Destination, boardCopy[Destination[0]][Destination[1]])

    if current[1] == '-':
        # There is no path from the source to the destination
        print(boardCopy)
        return None
    else:
        # Append the previously traversed coordinates from destination to source to the list until the source is reached
        while current[0] != Source:
            list.append(current[0])
            current = (current[1], boardCopy[current[1][0]][current[1][1]])

    list.append(current[0])
    # Reverse list to get shortest path coordinates in order from source to destination
    list.reverse()

    # Make a string of shortest path directions('R' = right, 'L' = left, 'D' = down, 'U' = up) from source to destination.
    directions = ''

    lastCoordinate = list[0]
    for index in range(1,len(list)):
        currentCoordinate = list[index]
        if lastCoordinate[1] + 1 == currentCoordinate[1]:
            directions = directions + 'R'
        elif lastCoordinate[1] - 1 == currentCoordinate[1]:
            directions = directions + 'L'
        elif lastCoordinate[0] + 1 == currentCoordinate[0]:
            directions = directions + 'D'
        elif lastCoordinate[0] - 1 == currentCoordinate[0]:
            directions = directions + 'U'
        lastCoordinate = currentCoordinate

    toReturn = (list, directions)

    return toReturn




# Hashtags are considered obstacles, while '-' are empty spaces that can be initialized with previously traversed coordinates on a path.
# You can modify the board by changing the amount of hashtags or '-'.
# Board can be modified to be any size M x N.
board = [['-','-','-','-','-'],
         ['-','-','#','-','-'],
         ['-','-','-','-','-'],
         ['#','-','#','#','-'],
         ['-','#','-','-','-']]

for row in board:
    print(row)

# For coordinate tuples, the left value is the row index and the right value is the column index. I.e. (0,1) means row 1 and column 2
# This is the starting coordinate of the desired path which you can modify.
source = (0,2)

# This is the final coordinate of the desired path which you can modify.
destination = (2,2)

print(solve_puzzle(board, source, destination))
