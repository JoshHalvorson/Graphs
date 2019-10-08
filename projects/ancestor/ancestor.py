# find node in values, check if key of that node is a value in another node. keep checking until get to node not in values
def earliest_ancestor(ancestors, starting_node, visited=None):
    values = []
    keys = []
    # build up the values list with the second value in the tuple.
    # this value is always a child, so we know there is a value connected to it
    # build keys list with the first value, these are all parent nodes
    for pair in ancestors:
        keys.append(pair[0])
        values.append(pair[1])
    # build visited set
    if visited is None:
        visited = set()
    # base case, if the node is not a child (in values) and it hasnt been visited (not part of the path)
    # return -1
    if starting_node not in values and starting_node not in visited:
        return -1
    # check the values for one == current node
    # if it finds it, add they key to visited, then cal the recursion
    # with the new starting node
    for pair in ancestors:
        if pair[1] == starting_node:
            visited.add(pair[0])
            return earliest_ancestor(ancestors, pair[0], visited)
    return starting_node

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 9))