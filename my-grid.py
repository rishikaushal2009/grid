import queue


def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", "O", " ", "#", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", "X", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze


def printMaze(maze, path=""):
    for j, row in enumerate(maze):
     for x, pos in enumerate(maze[j]):
    #for j, row in enumerate(maze):
    #    for i, col in enumerate(row):
    #     if maze[j][i] == "O":
        if pos == "O":
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
        if maze[j][i] != "X":   
           pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ "),
            else:
                print(col + " "),
        print()
        


def valid(maze, moves):
    #for x, pos in enumerate(maze[0]):
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
         if maze[j][i] == "O":
    #    if pos == "O":
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

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    #for x, pos in enumerate(maze[0]):
    for j, row in enumerate(maze):
        for i, col in enumerate(maze[j]):
         if maze[j][i] == "O":
    #    if pos == "O":
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

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze2()

while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)