class Graph {
    Map<Integer, Set<Integer>> edgeTo;

    Graph() {
        this.edgeTo = new HashMap<Integer, Set<Integer>>();
    }

    public int size() {
        return edgeTo.size();
    }

    public void addEdge(int v1, int v2) {
        add(v1, v2);
        add(v2, v1);
    }

    private void add(int from, int to) {
        if (!edgeTo.containsKey(from)) {
            Set<Integer> s = new HashSet<Integer>();
            s.add(to);
            edgeTo.put(from, s);
        } else {
            edgeTo.get(from).add(to);
        }
    }

    public Set<Integer> adj(int v) {
        return edgeTo.get(v);
    }
}

private Graph createGrap(char[][] matrix) {
    Graph g = new Graph();
    for (int r = 0; r < matrix.length; r++) {
        for (int c = 0; c < matrix[0].length; c++) {

            // skip this cells
            if (!isFreeCell(matrix[r][c])) {
                continue;
            }

            int id = createUniqueId(r, c);
            if (matrix[r][c] == 'S') {
                startVertex = id;
            } else if (matrix[r][c] == 'E') {
                endVertex = id;
            }
            createNeighbor(r, c, matrix, g);
        }
    }
    return g;
}

private void createNeighbor(final int r, final int c, final char[][] matrix2, final Graph g) {
    for (int row = -1; row <= 1; row++) {
        for (int col = -1; col <= 1; col++) {
            // avoid the center cell
            if (row ==0 && col == 0){
                continue;
            }
            // outside matrix
            if ((0 > c + col) || (c + col >= matrix2[0].length) || (0 > r + row) || (r + row >= matrix2.length)) {
                continue;
            }
            char value = matrix2[r+row][c+col];
            if (!isFreeCell(value)){
                continue;
            }
            int from = createUniqueId(r, c);
            int to = createUniqueId(row+r, col+c);
            g.add(from, to);
        }
    }

}

private boolean isFreeCell(char value) {
    return (value != '#' && value !='C');
}

private int createUniqueId(int r, int c) {
    return r * MAX_COL + c;
}

private void findSP(Graph g) {
    if (g == null || g.size() == 0) {
        throw new IllegalArgumentException("empty or null graph");
    }

    if (g.size() == 1) {
        throw new IllegalArgumentException(
                "graph's size must be greater than 1");
    }

    if (startVertex == -1) {
        throw new IllegalArgumentException("Start vertex not found");
    }

    if (endVertex == -1) {
        throw new IllegalArgumentException("End vertex not found");
    }

    Map<Integer, Integer> sonToParent = bfs(g, startVertex, endVertex);

    Stack<Integer> path = new Stack<Integer>();
    for (int son = endVertex; son!= startVertex; son = sonToParent.get(son)){
        path.push(son);
    }

       path.push(startVertex);
    while (!path.isEmpty()){
        System.out.print(path.pop() + ", ");
    }
}

private Map<Integer, Integer> bfs(Graph g, int startVertex2, int endVertex2) {
    Queue<Integer> q = new LinkedList<Integer>();
    Set<Integer> marked = new HashSet<Integer>();
    Map<Integer, Integer> sonToParent = new HashMap<Integer, Integer>();
    q.add(startVertex2);
    while (!q.isEmpty()) {
        int v = q.poll();
        for (Integer s : g.adj(v)) {
            if (!marked.contains(s)) {
                marked.add(s);
                sonToParent.put(s, v);

                if (s == endVertex2) {
                    return sonToParent;
                }

                q.add(s);
            }
        }

    }
    return null;
}