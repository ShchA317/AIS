from get_graph import get_graph

def dfs(v, finish, city_from, graph, prev):
    if prev[v] != "":
        return
    else:
        prev[v] = city_from
        if v == finish:
            return
        for neighbor in graph[v]:
            dfs(neighbor, finish, v, graph, prev)
            
def get_way(start, finish, prev):
    v = finish
    way = []
    while v != start:
        way.append(v)
        v = prev[v]
    way.append(start)
    return  list(reversed(way))
