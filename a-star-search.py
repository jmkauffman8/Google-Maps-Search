"""
Map Search
"""

import comp140_module7 as maps

class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._inner_data = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._inner_data)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        return str(self._inner_data)

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._inner_data.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        to_return = self._inner_data[0]
        self._inner_data.remove(to_return)
        return to_return

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._inner_data = []

class Stack:
    """
    A simple implementation of a LIFO stack.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._inner_data = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._inner_data)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        return str(self._inner_data)

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._inner_data.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        to_return = self._inner_data[-1]
        self._inner_data.remove(to_return)
        return to_return

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._inner_data = []

def bfs_dfs(graph, rac_class, start_node, end_node):
    """
    Performs a breadth-first search or a depth-first search on graph
    starting at the start_node.  The rac_class should either be a
    Queue class or a Stack class to select BFS or DFS.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - rac_class: a restricted access container (Queue or Stack) class to
          use for the search
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    dist = {}
    parent = {}
    for node in graph.nodes():
        #iterate through the nodes of the graph, redefining all distances
        #to infinity and parents to none
        dist[node] = float('inf')
        parent[node] = None
    dist[start_node] = 0
    queue_or_stack = rac_class()
    queue_or_stack.push(start_node)
    #push start_node into the queue or stack
    while len(queue_or_stack) >= 1:
        current_node = queue_or_stack.pop()
        for nbr in graph.get_neighbors(current_node):
            #iterate through the neighbors of current_node, redefining the
            #distance to be the distance from current node plus one, and
            #parent to be the current node
            if dist[nbr] == float('inf'):
                dist[nbr] = dist[current_node] + 1
                parent[nbr] = current_node
                queue_or_stack.push(nbr)
                #push neighbor into the queue to reiterate through graph
            for vertice, par in parent.items():
                if vertice == end_node and par != None:
                    #iterate through the items of parent, returning parent
                    #if the end_node has a parent
                    return parent
    return parent
print(bfs_dfs(maps.load_test_graph('line'), Queue, 'A', 'E'))
print(bfs_dfs(maps.load_test_graph('asymmetric1'), Queue, 'A', 'K'))
print(bfs_dfs(maps.load_test_graph('grid'), Stack, 'A', 'I'))
print(bfs_dfs(maps.load_test_graph('asymmetric2'), Queue, 'B', 'D'))
print(bfs_dfs(maps.load_test_graph('line'), Stack, 'A', 'E'))
def dfs(graph, start_node, end_node, parent):
    """
    Performs a recursive depth-first search on graph starting at the
    start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - parent: a dictionary that initially has one entry associating
                  the original start_node with None

    Returns: the modified parent dictionary which maps each visited node
    to its parent node
    """
    #define base case of start node equaling end node, returning parent if true
    if start_node == end_node:
        return parent
    #otherwise, iterate through unexplored neighbors of start_node
    else:
        for nbr in set(graph.get_neighbors(start_node)).difference(set(parent.keys())):
            #check if end_node is in parent, if not add nbr as a key in parent, with
            #start_node as its corresponding value, and call dfs to run again
            if end_node not in parent:
                parent[nbr] = start_node
                dfs(graph, nbr, end_node, parent)
    return parent
print('===')
print(dfs(maps.load_test_graph('line'), 'A', 'E', {'A': None}))
def astar(graph, start_node, end_node,
          edge_distance, straight_line_distance):
    """
    Performs an A* search on graph starting at start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - edge_distance: a function which takes two nodes and a graph
                         and returns the actual distance between two
                         neighboring nodes
        - straight_line_distance: a function which takes two nodes and
                         a graph and returns the straight line distance 
                         between two nodes

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    parent = {start_node: None}
    open_set = [start_node]
    closed_set = []
    #define parent to be a dictionary with the start_node mapped to null, open_set to 
    #be a listwith only start_node, and closed_set to be an empty list
    g_dict = {start_node: 0}
    h_dict = {start_node: straight_line_distance(start_node, end_node, graph)}
    min_node = None
    #define g_dict to be a dictionary with start_node mapped to 0, h_dict to be
    #a dictionary with start_node mapped to the straight line distance
    while len(open_set) >= 1:
        global_min = float("inf")
        #while open_set is not empty, iterate through its nodes
        for node in open_set:
            if g_dict[node] + h_dict[node] < global_min:
                global_min = g_dict[node] + h_dict[node]
                min_node = node
                #check to see if g_cost and h_cost of the node are less than the
                #global min, if so, redefine global_min to the sum of the two costs
                #(the f cost) and redefine min_node to node
        open_set.remove(min_node)
        closed_set.append(min_node)
        #remove min_node from open_set and add min_node to closed_set
        if min_node == end_node:
            return parent
        #return parent if mid_node is the same as end_node
        for nbr in graph.get_neighbors(min_node):
            if nbr in open_set:
                g_value = g_dict[min_node] + edge_distance(min_node, nbr, graph)
                if g_value < g_dict[nbr]:
                    #for the neighbors of min_node, define g_value to be the original
                    #g cost plus the edge distance from min_node to neighbor, and
                    #check if neighbor is in open_set
                    g_dict[nbr] = g_value
                    h_dict[nbr] = straight_line_distance(nbr, end_node, graph)
                    parent[nbr] = min_node
                    #map nbr to g_value in g_dict, nbr to the straight line distance from
                    #nbr to end_node in h_dict and nbr to min_node in parent
            elif nbr not in closed_set:
                g_dict[nbr] = g_dict[min_node] + edge_distance(min_node, nbr, graph)
                h_dict[nbr] = straight_line_distance(nbr, end_node, graph)
                #if nbr is not in closed set, map nbr to be the original g cost plus the
                #edge distance from min_node to neighbor in g_dict and map nbr to be the
                #straight line distance from nbr to end_node in h_dict
                open_set.append(nbr)
                parent[nbr] = min_node
                #add nbr to the open set and map nbr to min_node in parent
    return parent
# You can replace functions/classes you have not yet implemented with
# None in the call to "maps.start" below and the other elements will
# work.

maps.start(bfs_dfs, Queue, Stack, dfs, astar)
