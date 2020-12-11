# Note: this is basically a directed graph node. Edges are not directly 
# represented, only vertices. An inbound edge is implied when one vertex is in 
# the contained_by/superior adjacency list. An outbound edge is implied by the 
# contains/subordinate list.
class Node:
    def __init__(self, label):
        self.label = label
        self.contains = set() # So I don't have to both checking uniqueness
        self.contained_by = set()
        self.marked = False # For traversal
    
    def add_subordinate(self, node):
        self.contains.add(node)

    def add_superior(self, node):
        self.contained_by.add(node)

    # Make hashable (by label)
    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)

    def __repr__(self):
        # Make print decently for debugging
        return f'<Node: {self.label}>'

class Graph:
    def __init__(self):
        self.nodes = {}  # Nodes are keyed by label for easy lookup (we don't have too many)
    
    def add_node(self, node):
        self.nodes[node.label] = node
    
    def add_edge(self, source, dest):
        # Create an edge pointing from source to destination
        source.add_subordinate(dest)
        dest.add_superior(source)
    
    def __contains__(self, label):
        # Implement the "in" operator
        return label in self.nodes

    def get_node(self, label):
        if label in self.nodes:
            return self.nodes[label]
        else:
            return None

def read_data():
    g = Graph()
    with open('day07/input') as f:
        for line in f:
            # Separate superior (subject) from subordinate(s) (object(s))
            t = line.strip().split('contain')
            ind = t[0].find('bags')
            # Substring excluding space before 'bags'
            sup_label = t[0][0:ind - 1]
            if sup_label in g:
                sup = g.get_node(sup_label)
            else:
                sup = Node(sup_label)
                g.add_node(sup)

            
            items = t[1].split(',')  # If no comma, returns a list with one object so we're good
            for item in items:
                # Each item is of the form " n label bag(s)", so we start from 
                # index 3.
                label = item[3:item.find('bag') - 1]
                if label in g:
                    sub = g.get_node(label)
                else:
                    sub = Node(label)
                    g.add_node(sub)
                # Don't need to check for duplicate bc using sets for adjacency 'list'
                g.add_edge(sup, sub)

    return g


def part1():
    g = read_data()

    root = g.get_node('shiny gold')  # Find our bag
    root.marked = True
    
    # Try to write graph traversal from memory
    # We want to climb "up" to touch all nodes who eventually contain our root 
    # exactly once.
    # Looks like I wrote a depth-first approach and this is actually a stack
    count = 0
    queue = [n for n in root.contained_by]
    for n in queue:
        n.marked = True
    while queue:
        n = queue.pop()
        n.marked = True
        count += 1

        for adj in n.contained_by:
            if not adj.marked:
                queue.append(adj)
                # adj.marked = True # Need to make sure nodes are not re-added

    print(f'Part 1 answer: {count}')


if __name__ == '__main__':
    part1()
