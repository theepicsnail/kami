class UF:
    def __init__(self):
        self.roots = set()
        self.parents = dict()

    def __ensure(self, node):
        """ Ensure that a node is in the UF structure """
        if node not in self.parents:
            self.parents[node] = node
            self.roots.add(node)

    def union(self, nodeA, nodeB):
        self.__ensure(nodeA)
        self.__ensure(nodeB)

        self.parents[nodeA] = nodeB
        self.roots.remove(nodeA)

    def get_root(self, node):
        self.__ensure(node)

        parent = self.parents[node]
        if parent != node:
            parent = self.get_root(parent)
            self.parents[node] = parent

        return parent

    def get_roots(self):
        return self.roots
