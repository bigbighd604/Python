#!/usr/bin/env python
#
# Q. find out shortest path from a Node to any other Nodes
# Requirements:
# 1. no negative weights between two nodes
# 2. Dijkstra algorithm (http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
#


import sys


parents = {}
vertices = []
visited = set()

def ReadGraphMatrix(file_name):
  graph = {}
  file_object = open(file_name, "r")
  for line in file_object.readlines():
    vertex, matrix = line.rstrip().split(':')
    graph[vertex] = matrix.split(',')
  return graph


def ReadGraph(file_name):
  graph = {}
  weight = {}
  file_object = open(file_name, "r")
  for line in file_object.readlines():
    vertex, neighbors_weight = line.rstrip().split(':')
    vertex = int(vertex)
    graph[vertex] = []
    weight[vertex] = {}
    for i in neighbors_weight.split(','):
      neighbor, weigh = i.split('!')
      neighbor = int(neighbor)
      graph[vertex].append(neighbor)
      weight[vertex][neighbor] = int(weigh)
  return graph, weight


def D(s, graph, weight):
  visited = set()
  parents = {s:None}
  dist = {s:0}


  while True:
    min_node = None
    min_dist = 0
    for c in graph:
      if c not in visited and (min_node is None or
                               min_dist > dist.setdefault(c, 100000)):
        min_node = c
        min_dist = dist[c]

    if min_node is None:
      break
    visited.add(min_node)
    for i in graph[min_node]:
      if i not in dist:
        dist[i] = min_dist + weight[min_node][i]
        parents[i] = min_node
      elif dist[i] > min_dist + weight[min_node][i]:
        dist[i] = min_dist + weight[min_node][i]
        parents[i] = min_node

  return parents, dist


def PrintPathTo(node, parents):
  path = []
  while parents[node] != None:
    path.append(node)
    node = parents[node]
  path.append(0)
  path.reverse()
  return path


def DFS(root, graph):
  visited.add(root)
  pass


if __name__ == "__main__":
  graph,weight = ReadGraph(sys.argv[1]) # use weighed_graph.txt
  node = int(sys.argv[2])
  print 'graph: %s' % graph
  print 'Weight: %s' %weight
  parents,dist = D(0, graph, weight)
  path = PrintPathTo(node, parents)
  print 'Path from 0 to %s: %s' % (sys.argv[2], path)
