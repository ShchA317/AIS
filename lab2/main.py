from xmlrpc.client import MAXINT
from get_graph import get_graph, get_he_graph
import algs.bfs as bfs
import algs.dfs as dfs
import algs.limited_level_bfs as limited_level_bfs
import algs.limited_level_dfs as limited_level_dfs
import algs.dfs_iterative_deep as dfs_iterative_deep
import algs.bi_directional_search as bi_directional_search
import algs.greedy as greedy
import algs.a_star as a_star

graph = get_graph()
color = {}
distance = {}
prev = {}

for key in graph:
    prev[key] = ""
    color[key] = 0
    distance[key] = MAXINT


finish = "Казань"
start = "Брест"
level = 3

print("Let's get a trip from " + start + " to " + finish)

bfs.bfs(start, graph, color, distance)
dfs.dfs(start, finish, "", graph, prev)
limited_level_bfs.bfs_level(start, graph, color, distance, level)
limited_level_dfs.dfs_limit(start, finish, "", graph, prev, level, 0)
dfs_iterative_deep.dfs_iterative_deep(start, finish, graph)
# [print(f"{key} =>  {distance[key]}") for key in distance]
bfsWay = bfs.get_way(start, finish, distance, graph)
dfsWay = dfs.get_way(start, finish, prev)
limitedLevelBFS = limited_level_bfs.get_way(start, finish, distance)
limitedLevelDFS = limited_level_dfs.get_way(start, finish, prev)
dfsIterativeDeep = dfs_iterative_deep.get_way(start, finish, prev)
biDirectionalSearch = bi_directional_search.bi_directional_search(start, finish, graph)

print("Stage 1. Uninformative search")
print("Way by BFS: ", bfsWay)
print("Way by DFS: ", dfsWay)
print("Way by limited level BFS: ", limitedLevelBFS)
print("Way by limited level DFS: ", limitedLevelDFS)
print("Way by dfs iterative deep: ", dfsIterativeDeep)
print("Way by bidirectional search: ", biDirectionalSearch)
print()
print("Stage 2. Informative seach")

he_graph = get_he_graph()
greedyWay, greedyDist = greedy.greedy(start, finish, graph, he_graph)

print("Way by greedy search: ", greedyWay, " distation: ", greedyDist)

aStarWay, aStarDist = a_star.a_star(start, finish, graph, he_graph)

print("Way by A* search ", aStarWay, " distation: ", aStarDist)
