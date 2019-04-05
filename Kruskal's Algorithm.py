def mst(input_file):
    file = open(input_file, 'r', encoding="utf8")

    number_of_nodes = int(file.readline())

    names = []
    path = []
    sets = []

    for k in range(number_of_nodes):
        name_of_node = file.readline().split()
        names.append(name_of_node)
        sets.append(set([str(k+1)]))
        number_of_edges = int(file.readline())
        for l in range(number_of_edges):
            split_line = file.readline().split()
            line = [k+1, int(split_line[0]), int(split_line[1])]
            path.append(line)

    path.sort(key=lambda x: x[2])

    for i in path:
        for p in path:
            if i[0] == p[1] and i[1] == p[0] and i[2] == p[2]:
                path.remove(p)

    mst = 0
    edges = []
    for e in path:
        from_edge = set([str(e[0])])
        to_edge = set([str(e[1])])
        weight = e[2]
        for s in sets:
            if from_edge.issubset(s):
                index_from_edge = sets.index(s)
            if to_edge.issubset(s):
                index_to_edge = sets.index(s)
        while len(sets) != 1 and index_from_edge != index_to_edge:
            edges1 = [e[0], e[1], e[2]]
            edges.append(edges1)
            sets[index_from_edge] = sets[index_from_edge].union(sets[index_to_edge])
            sets.remove(sets[index_to_edge])
            mst += weight
            break

    for t in edges:
        print("From node:", names[t[0]-1], "To Node:", names[t[1]-1], "Weight:", t[2])
    print("The Lenght of Minimum Spanning Tree:", mst)

mst('tr_cities_names.txt')