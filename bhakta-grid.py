def find_shortest_path(grid, start_node, end_node):
    #take care of obvious cases
    if len(grid) == 0:
        return []
    if start_node == end_node:
        return [start_node]
       
    path = []
    # 4 possible neighbors (offsets)
    neighbors = {(1, 0), (-1, 0), (0, 1), (0, -1)}

    # our working queue
    queue = {start_node}
    # track distance of each node from start-node
    dists = {start_node: 0}
       # track prev-node that was used to get to the current node
    prevNodes = {}
    while queue:
        node = queue.pop()
        if not node:
            continue
        for dn in neighbors:
            nx = node.position.x + dn[0]
            ny = node.position.y + dn[1]
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                continue
            nnode = grid[nx][ny]
                       # check if we can pass through the node
            if not nnode.passable:
                continue
            distFromStart = dists[node] + 1
            if distFromStart >= dists.get(end_node, float('inf')):
                # if we are already farther from the shortest computed distance, then abandon this path
                continue
            if distFromStart < dists.get(nnode, float('inf')):
                # We found a better path to this node. Save it!
                dists[nnode] = distFromStart
                queue.add(nnode)
                # Save how we got to this node, we will use this eventually to back-track
                prevNodes[nnode] = node

    # find the optimum path backward
    if end_node in prevNodes:
        path.append(end_node)
        point = prevNodes[end_node]
        while point != start_node:
            path.append(point)
            point = prevNodes[point]
        path.append(start_node)
    # send it back reversed!
    return path[::-1]