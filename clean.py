# pick a level to run.
from levels import level1 as level
from collections import defaultdict,namedtuple

class Node(namedtuple("Node", ['color', 'num'])):
    def __str__(self):
        return "({}, {})".format(self.color, self.num)

def connect(graph, node, node2):
    graph[node].add(node2)
    graph[node2].add(node)

def disconnect(graph, node, node2):
    graph[node].remove(node2)
    graph[node2].remove(node)


def build_graph(level):
    graph = defaultdict(set) # Node -> set(Node)

    lastRow = None
    lastNode = None
    for row_id, level_row in enumerate(level):
        row = []
        for col_id, val in enumerate(level_row):
            node = Node(val, row_id * 10 + col_id)
            if col_id != 0:
                connect(graph, node, lastNode)
            if row_id != 0:
                connect(graph, node, lastRow[col_id])
            row.append(node)
            lastNode = node
        lastRow = row
    return graph

def compact(graph):
    for node in graph.keys():
        # needs_compacted = there might be a neighbor that's the same color
        needs_compacted = True
        while needs_compacted:
            needs_compacted = False
            for neighbor in list(graph[node]): # need a copy since we're mutating it.
                if neighbor.color == node.color:
                    needs_compacted = True # Well we found a match, we'll do another pass
                    for grandchild in list(graph[neighbor]):
                        connect(graph, node, grandchild)
                        disconnect(graph, neighbor, grandchild)
            # and now do another pass if we found a matching color.

    return graph # returns the same reference as the input, but makes this chainable foo(compact(bar(..)))

graph = build_graph([
    "rrb",
    "bbb",
    "brr",
])

graph = compact(graph)
for k,v in graph.items():
    print "%s => %s" % ( k, ", ".join(map(str,v)))

