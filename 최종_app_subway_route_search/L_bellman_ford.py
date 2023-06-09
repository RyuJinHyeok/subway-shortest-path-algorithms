import json

# set INF value
INF = 9999999

# bellman-ford algorithm
def bellman_ford(graph, start, end):
    # init
    dist = {(station, line) : INF if station != start else 0 for station in graph.keys() for line in graph[station].keys()}
    parent = {(station, line) : None for station in graph.keys() for line in graph[station].keys()}

    # caculate distance
    n = len(dist)
    for _ in range(n - 1):
        for parent_station in dist.keys():
            for station, line, cost in graph[parent_station[0]][parent_station[1]]:
                child_station = (station, line)
                if dist[child_station] > dist[parent_station] + cost:
                    dist[child_station]  = dist[parent_station] + cost
                    parent[child_station] = parent_station


    min_cost = INF
    min_line = None
    for line in graph[end].keys():
        if dist[(end, line)] < min_cost:
            min_cost = dist[(end, line)]
            min_line = line
            
    
    node = (end, min_line)
    path = []
    while node[0] != start:
        path.append(node)
        node = parent[node]
    path.append(node)
    path.reverse()

    return min_cost, path