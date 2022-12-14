from get_graph import get_graph, get_he_graph
from queue import PriorityQueue


def heuristic(v, he_graph):
    return he_graph[v]


def greedy(start, finish, graph, he_graph):
   pqueue = PriorityQueue()
   pqueue.put(start, 0)
   prev = {}
   prev[start] = None

   while not pqueue.empty():
      v = pqueue.get()

      if v == finish:
         break
      
      for neighbor in graph[v]:
         if neighbor not in prev:
            priority = heuristic(neighbor, he_graph)
            pqueue.put(neighbor, priority)
            prev[neighbor] = v
   return get_way(start, finish, prev, graph)         
      
def get_way(start, finish, prev, graph):
   v = finish
   way = []
   way_long = 0
   while v != start:
      way.append(v)
      way_long += graph[v][prev[v]]
      # print(graph[v][prev[v]])
      v = prev[v]
   # way += graph[v][start]
   way.append(start)
   return  list(reversed(way)), way_long

