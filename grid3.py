import queue

'''
def grid1():
    grid = []
    grid.append(["#","#", "#", "#", "#", "S","#"])
    grid.append(["#"," ", " ", " ", "#", " ","#"])
    grid.append(["#"," ", "#", " ", "#", " ","#"])
    grid.append(["#"," ", "#", " ", " ", " ","#"])
    grid.append(["#"," ", "#", "#", "#", " ","#"])
    grid.append(["#"," ", " ", " ", "#", " ","#"])
    grid.append(["#","#", "#", "#", "#", "E","#"])

    return grid
'''
def grid1():
    grid = []
    grid.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    grid.append(["#"," ", "#", " ", "#", " ", " ", " ", "#"])
    grid.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    grid.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    grid.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    grid.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    grid.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    grid.append(["#"," ", " ", " ", " ", " ", " ", "#", "#"])
    grid.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return grid

def grid3():
    grid = []
    grid.append(["#"," ","#","#"," "])
    grid.append([" ","#"," "," "," "])                
    grid.append([" ","#"," ","#"," "])                
    grid.append([" "," "," ","#"," "])                   
    grid.append([" "," "," ","#","#"]) 
    
    return grid



#print("please provide coordinates of start & end in grid")

class node:
    def __init__(self, a, b):
        #self.x = input("x : ")
        self.x=a
        #self.y = input("y : ")
        self.y=b

#print("starting node :-")
start_node = node(0,0)
#print("ending node: - ")
end_node = node(4,4)

'''
start_node.x=1
start_node.y=2
end_node.x=7
end_node.y=7
'''

def print_grid(grid):
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            print (grid[j][i]),
        print("")
    print("\n")



def printGRID(grid, path=""):
    start = 0 
    j1 = 0
    for j, row in enumerate(grid):
        for x, pos in enumerate(grid[j]):   
            if pos == "S":
                start = x
                j1 = j

    i = start
    j = j1
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        if grid[j][i] != "E":   
            pos.add((j, i))
    
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            if (j, i) in pos:
                grid[j][i]="+"
            '''    
            else:
                print(col + " "),
        print()
        '''
    print_grid(grid)         


def valid(grid, moves):
    start = 0 
    j1 = 0
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            if grid[j][i] == "S":
                start = i
                j1 = j

    i = start
    j = j1
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(grid[0]) and 0 <= j < len(grid)):
            return False
        elif (grid[j][i] == "#"):
            return False

    return True


def find_path(grid, moves, start_node, end_node):
    start = 0 
    j1 = 0
    for j, row in enumerate(grid):
        for i, col in enumerate(grid[j]):
            if grid[j][i] == "S":    
                start = i
                j1 = j

    i = start
    j = j1
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if grid[j][i] == "E":
        print("GotPath: " + moves)
        printGRID(grid, moves)
        return True

    return False


grid  = grid3()

grid[start_node.x][start_node.y]="S"
grid[end_node.x][end_node.y]="E"

#print_grid(grid)

def find_shortest_path(grid, start_node, end_node ):
    nums = queue.Queue()
    nums.put("")
    add = ""
    while not find_path(grid, add, start_node, end_node): 
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(grid, put):
                nums.put(put)


find_shortest_path(grid, start_node, end_node)