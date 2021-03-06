# Note: this is basically a directed graph node. Edges are not directly 
# represented, only vertices. An inbound edge is implied when one vertex is in 
# the contained_by/superior adjacency list. An outbound edge is implied by the 
# contains/subordinate list.
class Node:
    def __init__(self, label):
        self.label = label
        self.contains = {}  # Need to record subordinate label *and* count
        self.contained_by = set()  # So I don't have to both checking uniqueness
        self.marked = False  # For traversal
        self.total = 0
    
    def add_subordinate(self, node, count):
        # Subordinates are uniquely defined so we still don't need to error check
        self.contains[node] = count

    def add_superior(self, node):
        # Don't need to check for duplicate bc using sets for adjacency 'list'
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
    
    def add_edge(self, source, dest, count):
        # Create an edge pointing from source to destination
        source.add_subordinate(dest, count)
        dest.add_superior(source)
    
    def __contains__(self, label):
        # Implement the "in" operator
        return label in self.nodes

    def get_node(self, label):
        if label in self.nodes:
            return self.nodes[label]
        else:
            return None

def read_data(file):
    g = Graph()
    with open(f'day07/{file}') as f:
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
                if item == ' no other bags.':
                    continue
                # Each item is of the form " n label bag(s)", so we start from 
                # index 3.
                label = item[3:item.find('bag') - 1]
                count = int(item[1]) # Always 1 char
                if label in g:
                    sub = g.get_node(label)
                else:
                    sub = Node(label)
                    g.add_node(sub)
                
                g.add_edge(sup, sub, count)

    return g


def part1():
    g = read_data('input')

    root = g.get_node('shiny gold')  # Find our bag
    root.marked = True
    
    # Try to write graph traversal from memory
    # We want to climb "up" to touch all nodes who eventually contain our root 
    # exactly once.

    # Clarification (hopefully in better mathematical language): We want to 
    # traverse the subgraph of all components that are "upstream" of root and 
    # count the number of members (not including root), that is, all nodes n 
    # such that n is connected to root only by subordinate edges, i.e. all edges 
    # in the path n -> root go in the direction superior -> subordinate, and all
    # nodes in said path are unique.

    # Looks like I wrote a depth-first approach and this is actually a stack
    count = 0
    queue = [n for n in root.contained_by]
    for n in queue:
        n.marked = True

    while queue:
        n = queue.pop()
        count += 1

        for adj in n.contained_by:
            if not adj.marked:
                queue.append(adj)
                adj.marked = True # Need to make sure nodes are not re-added

    print(f'Part 1 answer: {count}')


# This problem is interesting because the counts are not uniquely defined for
# each bag type, but rather only in the context of how many of X bags a bag of 
# type Y contains. Thus, they are essentially the edge labels in our graph, and 
# are thus stored in the subordinate "list" which is now a dictionary. I realize 
# now that this kind of weird structure has resulted in probably a lot of 
# duplicated edges, but who cares, the problem is small and it works (well, at 
# least part 1 did at the time of writing this comment).

# Traverse in much the same way, but this time downstream. We need to
# recursively get the  total count of each node.
def get_count(node):
    if not node.contains:  # End node
        return 0
    else:
        count = 0
        for n in node.contains:
            if n.total == 0 and not n.marked:  # Unvisited, must calculate
                n.total = get_count(n)
                n.marked = True
            # The current bag contains x bags of type n, plus x * the count of 
            # bags contained by each bag of type n
            count += node.contains[n] * (n.total + 1)
        return count

def part2():
    g = read_data('input')

    root = g.get_node('shiny gold')  # Find our bag
    root.marked = True
    print(f'Part 2 answer: {get_count(root)}')


if __name__ == '__main__':
    part1()
    part2()
