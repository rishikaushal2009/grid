import queue



def printGRID(grid4, grid4_start, grid4_target ,  path=""):
    start = 0
    j1 = 0
    for j, row in enumerate(grid4):
        for x, pos in enumerate(grid4[j]):
            if grid4[j][x] == grid4_start :
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
        if grid4[j][i] != grid4_target:
             pos.add((j, i))
    for j, row in enumerate(grid4):
        for i, col in enumerate(row):
                if (j, i) in pos:
                    print(" + ",end="")
                    #grid4[j][i]=" + "
                    #print("Traverse ({}, {})".format(j, i))
                else :
                    print(grid4[j][i],end="") 
        print("")               

         

def valid(grid4, moves, grid4_start, grid4_target):
    start = 0
    j1 = 0
    for j, row in enumerate(grid4):
        for i, col in enumerate(row):            
             if grid4[j][i] == grid4_start :
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
        if not(0 <= i < len(grid4[0]) and 0 <= j < len(grid4)):
            return False
        elif (not grid4[j][i].passable):
            return False

    return True


def find_path(grid4, moves, grid4_start, grid4_target):
    start = 0
    j1 = 0
    for j, row in enumerate(grid4):
         for i, col in enumerate(grid4[j]):
            if grid4[j][i] == grid4_start :
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

        if grid4[j][i] == grid4_target :
            printGRID(grid4,grid4_start, grid4_target , moves)
            res = []
            x = grid4_start.position.x
            y = grid4_start.position.y
            res.append(grid4[y][x])
            for move in moves :
                #k=len(moves)-i
                if move == "D":
                    y += 1
                elif move == "R":
                    x += 1
                elif move == "L":
                    x -= 1
                elif move == "U":
                    y -= 1
                res.append(grid4[y][x])
#         res.append((end_node.x, end_node.y))
            #print("Res = {t}".format(t=res))
            return True, res

    return False, []




def find_shortest_path(grid4, grid4_start, grid4_target):
    if len(grid4) == 0:
        return []
    #print_grid(grid4)
    nums = queue.Queue()
    nums.put("")
    add = ""
    found = False
    res = []
    while not found:
        found, res = find_path(grid4, add, grid4_start, grid4_target)
        if not found:
            add = nums.get()
            for j in ["L", "R", "U", "D"]:
                put = add + j
                if valid(grid4, put, grid4_start, grid4_target):
                    nums.put(put)
    return res




'''
def find_shortest_path(grid4, grid4_start, grid4_target):
    if len(grid4) == 0:
        return []
    nums = queue.Queue()
    nums.put("")
    add = ""
    found = False
    res = []
    f=0
    while not found:
        start = 0
        j1 = 0
        if f=0 moves=add else moves=put
        for j, row in enumerate(grid4):
            for i, col in enumerate(grid4[j]):
                if grid4[j][i] == grid4_start :
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

            if grid4[j][i] == grid4_target :
                res = []
                x = grid4_start.position.x
                y = grid4_start.position.y
                res.append(grid4[y][x])
                for move in moves :
                    #k=len(moves)-i
                    if move == "D":
                        y += 1
                    elif move == "R":
                        x += 1
                    elif move == "L":
                        x -= 1
                    elif move == "U":
                        y -= 1
                    res.append(grid4[y][x])
#         res.append((end_node.x, end_node.y))
            #print("Res = {t}".format(t=res))
                found = True
                return res
            else :
                add = nums.get()
                f=1
                for j in ["L", "R", "U", "D"]:
                    put = add + j
                    if not(0 <= i < len(grid4[0]) and 0 <= j < len(grid4)):
                        continue
                    elif (not grid4[j][i].passable):
                        continue
                    else :
                        nums.put(put)
                        add = put
'''
            
            
            






