from util import Stack, Queue

class GraphNode:
    def __init__(self, value):
        self.children = set()
        self.parents = set()
        self.value = value

    def add_child(self, node):
        self.children.add(node)
        node.parents.add(self)

    def __repr__(self):
        children = [x.value for x in self.children]
        parents = [x.value for x in self.parents]
        return f'Node: {self.value} children {children} parents {parents}'

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_node(self, value):
        if self.vertices.get(value, None) is None:
            self.vertices[value] = GraphNode(value)
        else:
            return False

    def add_edge(self, value1, value2):
        if value1 not in self.vertices:
            self.add_node(value1)
        if value2 not in self.vertices:
            self.add_node(value2)
        node1 = self.vertices[value1]
        node2 = self.vertices[value2]
        node1.add_child(node2)

    def get_node(self, value):
        return self.vertices.get(value, None)

    def ancestor_paths(self, value):
        node = self.get_node(value)
        if node is None:
            return None
        s = Stack()
        s.push([value])

        ancestor_paths = []

        while s.size() > 0:
            path = s.pop()
            node = self.get_node(path[-1])
            for parent_node in node.parents:
                new_path = path.copy()
                new_path.append(parent_node.value)
                s.push(new_path)
                ancestor_paths.append(new_path)

        return ancestor_paths

        def __repr__(self):
            for value in self.vertices:
                print(self.vertices[value])

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for pair in ancestors:
        parent_value = pair[0]
        child_value = pair[1]
        g.add_edge(parent_value, child_value)

    ancestor_paths = g.ancestor_paths(starting_node)

    longest_path = []
    for path in ancestor_paths:
        if len(path) > len(longest_path):
            longest_path = path
        elif len(path) == len(longest_path)
        if path[-1] < longest_path[-1]:
            longest_path = path

    if len(longest_path) == 0:
        return -1
    else:
        return longest_path