"""
Problem:
We are given a black&white image which is represented by a matrix with 0 representing black pixle 
and 1 representing white pixle. Our objective is to remove the black pixles which are not linked to the
border. These black pixles that forms 'island' has to be removed.

Sample input: 
[
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

Sample output:
[
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

(Source: https://www.youtube.com/watch?v=4tYoVx0QoN0)
"""

input_matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

def removeIslands(matrix):
    edgeMap = {}

    def lookupForConnection(edgeMap, x, y, matrix):
        # Top
        if(x != 0 and matrix[x - 1][y] == 1):
            edgeMap['{}{}'.format(x-1,y)] = True
            lookupForConnection(edgeMap, x-1, y, matrix)

        # Bottom
        if(x != len(matrix) - 1 and matrix[x + 1][y] == 1):
            edgeMap['{}{}'.format(x+1,y)] = True

        # Left
        if(y != 0 and matrix[x][y - 1] == 1):
            edgeMap['{}{}'.format(x,y-1)] = True
            lookupForConnection(edgeMap, x, y-1, matrix)

        # Right
        if(y != len(matrix[x]) - 1 and matrix[x][y + 1] == 1):
            edgeMap['{}{}'.format(x,y+1)] = True

    for xCord, rows in enumerate(matrix):
        for yCord, rowItem in enumerate(rows):
            if (xCord == 0 or yCord == 0 or yCord == len(rows) - 1) and rowItem == 1:
                edgeMap['{}{}'.format(xCord, yCord)] = True

    
    for cord in edgeMap.copy():
        x = int(cord[0])
        y = int(cord[1])
        
        lookupForConnection(edgeMap, x, y, matrix)

    for xCord, rows in enumerate(matrix):
        for yCord, rowItem in enumerate(rows):
            if (rowItem == 1) and ('{}{}'.format(xCord, yCord) not in edgeMap):
                matrix[xCord][yCord] = 0

    return matrix


print(removeIslands(input_matrix))