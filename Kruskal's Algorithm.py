def read_file(input_file):  # This function provides 3 output list, in order to path, names, sets
    file = open(input_file, 'r', encoding="utf8")

    graph = []  # The edges and nodes store in this list
    name_of_nodes = []  # If exist name of nodes store in this list
    sets_of_nodes = []  # The sets of nodes store in this list

    for k in range(int(file.readline())):  # Iterate number of nodes time
        name_of_nodes.append(file.readline().split())  # Name of node added to 'names' list
        sets_of_nodes.append({str(k + 1)})
        for l in range(int(file.readline())):  # Iterate number of edges time
            split_line = file.readline().split()
            graph.append([str(k + 1), str(split_line[0]), int(split_line[1])])
    return graph, name_of_nodes, sets_of_nodes


def sort_remove(graph):  # This function sorts the edges due to weights and remove the same edges from graph
    for i in graph:  # This section removes identical edges
        for p in graph:
            if i[0] == p[1] and i[1] == p[0] and i[2] == p[2]:
                graph.remove(p)

    graph.sort(key=lambda x: x[2])  # Sort 2d graph list due to second element

    return graph


def find_mst(graph, sets_of_nodes):
    minimum_spanning_tree = 0  # initial Minimum Spanning Tree
    edges = []  # Edges in MST will stored here
    for e in graph:
        for s in sets_of_nodes:  # e[0] = from_node, e[1] = to_node, e[2] = weight
            if {e[0]}.issubset(s):
                index_from_edge = sets_of_nodes.index(s)  # Find index of from_node
            if {e[1]}.issubset(s):
                index_to_edge = sets_of_nodes.index(s)  # Find index of to_node
        if index_from_edge != index_to_edge and len(sets_of_nodes) != 1:  # Loop until MST computed
            edges.append([e[0], e[1], e[2]])
            sets_of_nodes[index_from_edge] = sets_of_nodes[index_from_edge].union(sets_of_nodes[index_to_edge])
            sets_of_nodes.remove(sets_of_nodes[index_to_edge])
            minimum_spanning_tree += e[2]
    return minimum_spanning_tree, edges


def minimum_st(input_file):
    path, names, sets = read_file(input_file)
    path = sort_remove(path)
    mst, edges = find_mst(path, sets)
    #for t in edges:
        #print("From node:", names[int(t[0]) - 1], "To Node:", names[int(t[1]) - 1], "Weight:", t[2])
    print("The Lenght of Minimum Spanning Tree:", mst)


minimum_st('tr_districts_IDs.txt')
