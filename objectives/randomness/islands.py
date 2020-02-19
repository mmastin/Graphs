# Write a function that takes a 2D binary array and returns the number 
# of 1 islands. An island consists of 1s that are connected to the north, 
# south, east or west. For example:

# island_counter(islands) # returns 4

# Translate into graph terminology
# build the graph
# transverse the graph

# Understand, Plan, Execute, Return(review?)

def island_counter(matrix):
    # create a visited matrix of same dimensions as given matrix
    visited = []
    island_count = 0
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # walk through each cell of matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # count up the connected components
            # if it has not been visited
            if not visited[y][x]:
                # when I reach a one:
                if matrix[y][x] == 1:
                    # do a dft and mark each 1 as visited
                    visited = dft(x, y, matrix, visited)
                    # increment the counter by 1
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def dft(col, row, matrix, visited):
    """
    this will mark each connect componenet as visited
    return visited matrix
    """
    s = Stack()
    s.push( (col, row) )
    while s.size() > 0:
        v = s.pop()
        col = v[0]
        row = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors((col, row), matrix): # STub
                s.push(neighbor)
    return visited

def get_neighbors(vertex, graph_matrix):
    col = vertex[0]
    row = vertex[1]
    neighbors = []
    # check north
    if row > 0 and graph_matrix[row - 1][col] == 1:
        neighbors.append((col, row - 1))
    # check south
    if row < len(graph_matrix) - 1 and graph_matrix[row + 1][col] == 1:
        neighbors.append((col, row + 1))
    # check east
    if col < len(graph_matrix[0]) - 1 and graph_matrix[row][col + 1] == 1:
        neighbors.append((col + 1, row))
    # check west
    if col > 0 and graph_matrix[row][col - 1] == 1:
        neighbors.append((col - 1, row))
    # return all directions that contain a 1
    return neighbors

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

islands2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


# print(get_neighbors((1, 4), islands))
print(island_counter(islands))
print(island_counter(islands2))