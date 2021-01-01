# Global variables, I intentionally leave the values as ... because # I don't have any meaningful values yet. But it won't affect how
# you understand the problem, I promise.
R, C = 3,3
m = ...
sr, sc = ...
rq, cq = ...
# Variables used to keep track of total number of steps to be taken
move_count = 0
nodes_left_in_layer = 0
nodes_in_next_layer = 1
# Variable to see whether we already reached at the end or not
reached_end = false
# Matrix to keep track of visited cells.
visited = ...
# North, South, East and West direction vectors
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

def solve():
    rq.enqueue(sr)
    cq.enqueue(sc)
    visited[sr][sc] = true
    
    while rq.size() > 0:
         r = rq.dequeue()
         c = cq.dequeue()
         if m[r][c] == 'E':
             reached_end = true
             break
         explore_neighbors(r, c)
         nodes_left_in_layer --
         if nodes_left_in_layer == 0:
              nodes_left_in_layer = nodes_in_next_layer
              nodes_in_next_layer = 0
              move_count ++
    if reached_end == true:
        return move_count
    return -1
function explore_neighbors(r, c):
    for(i=0; i<4: i++):
        rr = r + dr[i]
        cc = c + dc[i]
        
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
        
        if visited[r][c] == true:
            continue
        if m[r][c] == '#':
            continue
        
        rq.enqueue(rr)
        rc.enqueue(cc)
        visited[r][c] = true
        
        nodes_in_next_layer ++