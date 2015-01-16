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

    def draw(self):
        for node in self.nodes:
            out = "{}| ".format(str(node))
            out += " ".join(map(str, node.neighbors))
            print out

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

def graphviz(graph):
    symbolattrs = {
        "k": "gray",
        "r": "red",
        "y": "yellow",
        "w": "white",
    }

    def attrLine(node):
        gap = .51
        return "{}[shape=square,style=filled,fillcolor={}]".format(
            node._id, symbolattrs[node.symbol])

        return "{}[shape=square,style=filled,fillcolor={},pos=\"{},{}!\";fixedsize=true]".format(
            node._id, symbolattrs[node.symbol], node._id % 10 * gap, node._id/10 * -1 * gap)
    def neighborLine(node):
        fmt = "%s--%%s" % node._id
        edges = []
        for neighbor in node.neighbors:
            if neighbor._id < node._id: # only make one edge per connection
                continue
            edges.append(fmt % neighbor._id)
        if edges:
            return ";".join(edges) + ";"
        return ""

    attrs = ";".join(map(attrLine, graph.nodes))
    edges = "".join(map(neighborLine, graph.nodes))
    out = "graph g{%s;%s}" % (attrs,edges)
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


#levelPrinter(level)

graph = build_graph(level)
#print graphviz(graph, {
#    "r": "[shape=circle,style=filled,fillcolor=red]",
#    "b": "[shape=circle,style=filled,fillcolor=blue]",
#    "k": "[shape=circle,style=filled,fillcolor=gray]",
#})
compact(graph)
graph.removeOrphans()
print graphviz(graph)
#graph.draw()
# display non-orphaned nodes:
#for node in graph.nodes:
#    print str(node) +":" + " ".join(map(str, node.neighbors))


