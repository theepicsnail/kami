class Node(object):
    _id = 0 # Unique id for each node
    def __init__(self, symbol):
        self.symbol = symbol
        self.neighbors = []
        self._id = Node._id
        Node._id += 1

    def connect(self, other):
        """Make an undirected edge between two Nodes"""
        if other in self.neighbors:
            return # Already connected
        self.neighbors.append(other)
        other.neighbors.append(self)

    def disconnect(self, other):
        """Remove the undirected edge between two Nodes"""
        if other not in self.neighbors:
            return # Already disconnected
        self.neighbors = filter(lambda x:x != other, self.neighbors)
        other.neighbors = filter(lambda x:x != self, other.neighbors)
    # formatting stuff
    def __str__(self):
        return "[{} {:3}]".format(self.symbol, self._id)
    def __repr__(self):
        return str(self)

class Graph(object):
    def __init__(self):
        self.nodes = []

    def newNode(self, symbol):
        node = Node(symbol)
        self.nodes.append(node)
        return node

    def removeOrphans(self):
        for idx in xrange(len(self.nodes)-1, -1, -1):
            if not self.nodes[idx].neighbors:
                del self.nodes[idx]
        return self

    def draw(self):
        for node in self.nodes:
            out = "{}| ".format(str(node))
            out += " ".join(map(str, node.neighbors))
            print out

    def toDict(self):
        out = {}
        for node in self.nodes:
            nids = [(n.symbol, n._id) for n in node.neighbors]
            out[(node.symbol, node._id)] = set(nids)
        return out

def build_graph(level):
    graph = Graph()

    # create the nodes in the level
    # and store them in a 2d grid
    nodes = []
    for row in level:
        node_row = []
        nodes.append(node_row)
        for val in row:
            node = graph.newNode(val)
            node_row.append(node)

    # Connect all of the nodes to their neighbors
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            cur = nodes[row][col]
            if row != 0:
                cur.connect(nodes[row-1][col])
            if col != 0:
                cur.connect(nodes[row][col-1])
            if row != rows-1:
                cur.connect(nodes[row+1][col])
            if col != cols-1:
                cur.connect(nodes[row][col+1])

    return graph

def compact(graph):
    # compact the graph from
    # 0-0-0
    # | | |
    # 0-1-1
    # | | |
    # 0-1-2
    #
    # into
    # 0-1-2
    # by joining neighboring, same symbol nodes
    for node in graph.nodes:
        needs_compacted = True
        while needs_compacted:
            needs_compacted = False
            for neighbor in list(node.neighbors): # mutating this list, make a copy
                if neighbor.symbol == node.symbol:
                    # Found a mergable node
                    # 1) orphan it
                    # 2) connect all of its neigbors (except node itself) to node
                    for grandchild in list(neighbor.neighbors):
                        needs_compacted = True
                        neighbor.disconnect(grandchild)
                        if grandchild != node:
                            node.connect(grandchild)
    return graph

def graphviz(graph):
    symbolattrs = {
        "k": "gray",
        "r": "red",
        "y": "yellow",
        "w": "white",
        "b": "blue",
    }

    def attrLine(node):
        return "{}[shape=circle,style=filled,fillcolor={}]".format(
            node._id, symbolattrs[node.symbol])
    def neighborLine(node):
        fmt = "%s--%%s" % node._id
        edges = []
        for neighbor in node.neighbors:
            if neighbor._id < node._id: # only make one edge per connection
                continue
            edges.append(fmt % neighbor._id)
        if edges:
            return ";\n".join(edges) + ";\n"
        return ""
    attrs = ";\n".join(map(attrLine, graph.nodes))
    edges = "".join(map(neighborLine, graph.nodes))
    out = "graph g{\n%s;\n%s}" % (attrs,edges)
    return out

def levelPrinter(level):
    RESET       = "\033[0;0m"
    BLACK       = "\033[0;30m"
    RED         = "\033[0;31m"
    GREEN       = "\033[0;32m"
    YELLOW      = "\033[0;33m"
    BLUE        = "\033[0;34m"
    PURPLE      = "\033[0;35m"
    CYAN        = "\033[0;36m"
    LIGHT_GRAY  = "\033[0;37m"
    DARK_GRAY   = "\033[1;30m"
    LIGHT_RED   = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_YELLOW= "\033[1;33m"
    LIGHT_BLUE  = "\033[1;34m"
    LIGHT_PURPLE= "\033[1;35m"
    LIGHT_CYAN  = "\033[1;36m"
    WHITE       = "\033[1;37m"
    import sys
    color = {'r':RED, 'b':BLUE, 'k': DARK_GRAY, ' ':DARK_GRAY, 'y':YELLOW, 'w':LIGHT_GRAY}
    sys.stdout.write(RESET)
    print "0123456789"
    for row_num, row in enumerate(level):
        for val in row:
            sys.stdout.write(color[val])
            sys.stdout.write('#')
        sys.stdout.write(RESET)
        sys.stdout.write(' %s\n' % (row_num*10))



from collections import Counter, defaultdict
def getMoves(graph):
    """
    kkr
    rrr
    rkk

    graph = { (k, 0):[(r, 2)],
              (r, 2):[(k, 0), (k, 7)],
              (k, 7):[(r, 2)]}

    possible_moves = {
        2: [ ((r, 2), k) ], # middle reds into black has a score of 2
        1: [ ((k, 0), r)    # top black to red has a score of 1
           , ((k, 7), r)]   # bottom black to red has a score of 1
    }


    """
    possible_moves = defaultdict(list)
    for node, neighbors in graph.items():
        # Count the number of neighbors of each color this node has
        neigh_colors = Counter()
        for (symbol, _id) in neighbors:
            neigh_colors[symbol] += 1

        for (color, count) in neigh_colors.items():
            possible_moves[0].append((count, node, color))
    return possible_moves

def max_distance(node, graph):
    min_dist = {node:0}
    node_queue = [node]
    max_dist = 0
    while node_queue:
        node = node_queue.pop(0)
        dist = 1 + min_dist[node]
        for neighbor in graph[node]:
            if neighbor not in min_dist:
                min_dist[neighbor] = dist
                node_queue.append(neighbor)
                max_dist = max(dist, max_dist)
    return max_dist


def sort_by_max_distance(moves, graph):
    annotated_moves = []
    for move in moves:
        annotated_moves.append((max_distance(move[1], graph), move))
    import pdb; pdb.set_trace()
    return map(lambda (x,y):y, sorted(annotated_moves)) # sort and strip annotation

def getOrderedMoves(graph):
    moveDict = getMoves(graph)

    sorted_keys = sorted(moveDict.keys())
    out = []
    for key in sorted_keys[::-1]:
        moves = sort_by_max_distance(moveDict[key], graph)
        out.extend(moves)#moveDict[key])
    return out

def performMove(graph, move):
    """
    kkr
    rrr
    rkk

    graph = { (k, 0):[(r, 2)],
              (r, 2):[(k, 0), (k, 7)],
              (k, 7):[(r, 2), (B,11)]}
    move = (2, (r, 2), k)
    """
    score, node, newColor = move
    # 2,  (r, 2),  k

    newNode = (newColor, node[1])
    # (k, 2)
    # For each node of the changed node's neighbors:
    # if it's a different from the end color,
    #   add it to the newNeighbors set
    # else it's the same color and we need to merge:
    #   add all of the grandchildren to newNeighbors
    #   remove this node from each of the grandchildren
    #   delete this node
    #
    # now we have newNeighbors, a list of all the nodes that
    # should be connected to the new node.
    # point them all to this node

    newGraph = {}
    for k,v in graph.items():
        newGraph[k]=set(v)
    graph = newGraph
    newNeighbors = set()

    for neighbor in list(graph[node]):
        if neighbor[0] != newColor:
            newNeighbors.add(neighbor) # link it to the new node
            graph[neighbor].remove(node) # unlink it from the old
        else: #it's the same color. bring the grandchildren in.
            newNode = min(newNode, neighbor) # newNode should be the minimal node (deterministic output)
            for grandchild in graph[neighbor]:
                if grandchild == node: # skip the circular reference
                    continue
                newNeighbors.add(grandchild)
                graph[grandchild].remove(neighbor)

            del graph[neighbor] # all of the children are set to be re-added, and nothing points to this node now.
            # remove it.
    del graph[node] # same with the original node.
    # Add our new node, and its edges
    for changed in newNeighbors:
        graph[changed].add(newNode)
    graph[newNode] = newNeighbors

    return graph
def asdf():
    # graph = { (k, 0):[(k, 2],
    #           (r, 2):[(k, 0), (k, 7)],
    #           (k, 7):[(k, 2)]}

    graph[newNode] = graph[node]
    del graph[node]

    # graph = { (k, 0):[(k, 2],
    #           (k, 2):[(k, 0), (k, 7)],
    #           (k, 7):[(k, 2)]}

    # Find the root node (the node where the merge under, decided by minimal ID)

    # merge all of rootNode's children into root node. Because this is already a compacted graph, we don't need
    # to worry about following chains of same-colors
    newNeighbors = set(graph[newNode])
    print "Root node:", rootNode
    print "New node :", newNode
    print "Graph:", graph
    for neigh in graph[newNode]:
        print "  Neighbor:", neigh
        if neigh[0] != newColor:
            print "    added to newNeighbors"
            newNeighbors.add(neigh)
        else: # neigh needs merged in
            # because it's compacted we know
            # grandchild's color != neighbors color.
            # Since we got here, we know  neigh[0] == newColor
            # newColor == neigh[0] != granchilds color.
            # So all grandchildren can be merged in
            for grandchild in graph[neigh]:
                if grandchild == newNode:
                    continue
                print "    Grandchild:", grandchild
                newNeighbors.add(grandchild)
                print "       Added to newNeighbors"
                graph[grandchild].remove(neigh)
                graph[grandchild].add(newNode)
    return graph
#import pprint
#pprint.pprint(
#    getMoves(compact(build_graph(["kkr","rrr","rkk"])).removeOrphans().toDict())
#)
import pprint
def solve(graph, turns):
    if turns == 0:
        if len(graph) == 1:
            return []
        return None

    moves = getOrderedMoves(graph)
    for move in moves:
        #if turns > 7:
        #    print "  " * (8-turns), move
        g2 = performMove(graph, move)
        solution = solve(g2, turns-1)
        if solution is not None:
            return [move] + solution
    return None

def solve2(graph, turns):
    move_queue = [(graph,turns,[])]
    depth = 0
    seen_state = set()

    def graphhash(graph):
        out = ""
        for node in sorted(graph.keys()):
            out += str(node)
            for neighbor in sorted(graph[node]):
                out += str(neighbor)
            out += "|"
        return out

    def seen(state):
        return graphhash(state[0]) in seen_state

    def add(state):
        move_queue.append(state)
        seen_state.add(graphhash(state[0]))
    while move_queue:
        graph, turns, previous_moves = move_queue.pop(0)
        if depth != turns:
            #print turns
            depth = turns
        if len(graph) == 1:
            return previous_moves
        moves = getOrderedMoves(graph)
        for move in moves:
            g2 = performMove(graph, move)
            state = (g2, turns-1, previous_moves + [move])
            move_queue.append(state)
            #if not seen(state):
            #    add(state)
                # solved or not
    return []
    #g = performMove(graph, (2, ('w',115), 'k'))
    #g = performMove(g,    (2, ('k',5), 'y'))
    #g = performMove(g,    (2, ('y',2), 'r'))
    #g = performMove(g,    (2, ('r',0), 'w'))
    #pprint.pprint(g, width=200)
    #print len(g)
    #move = (2, (r, 2), k)

    #for idx, move in enumerate(moves):
    #    if idx % 5 == 0:
    #        print
    #    print move, "\t",

level = [
   #0123456789
   "rryyykkkww",#  0
   "rryyykkkww",# 10
   "rryyykkkww",# 20
   "rryyykkkkk",# 30
   "ryyyykrrkk",# 40
   "rwwrrkrrkk",# 50
   "rwwrrkrrkk",# 60
   "rwwrrkkkkk",# 70
   "ryyrrkkkkk",# 80
   "kkyrrkrryy",# 90
   "kkyrrkrryy",#100
   "kkyrrwrryy",#110
   "krryykyyrr",#120
   "krryykyyrr",#130
   "kkryykyyrr",#140
   "kkkkkkyyrr",#150
]
level2 = [
   #0123456789
   "bwbbrbbwbb",#  0
   "bwwbrrbwwb",# 10
   "wbbrbbrbbw",# 20
   "wwbrrbrrbw",# 30
   "bbrbbwbbrb",# 40
   "wbrrbwwbrr",# 50
   "bwbbwbbwbb",# 60
   "bwwbwwbwwb",# 70
   "wbbrbbrbbw",# 80
   "wwbrrbrrbw",# 90
   "bbrbbwbbrb",#100
   "rbrrbwwbrr",#110
   "bwbbrbbwbb",#120
   "bwwbrrbwwb",#130
   "rbbwbbrbbr",#140
   "rrbwwbrrbr",#150
]

#level = [
#    "rrk",
#    "kkk",
#    "krr",
#]

levelPrinter(level)
graph = build_graph(level)
compact(graph)
graph.removeOrphans()
#print >>file("out.dot","w"), graphviz(graph)
for move in solve(graph.toDict(), 4):
    print move
