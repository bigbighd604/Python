#!/usr/bin/env python
#
# Use A Star to find word ladder.
# heuristic function is the difference letters of 2 words.
#


from heapq import heappush, heappop
from string import ascii_lowercase as chars


inf = float('inf')
global counter # How many words examined to find a path.

def a_star(graph, start, target, heuristic):
  global counter
  counter = 0
  parents, queue = {}, [(heuristic(start), None, start)]
  while queue:
    counter += 1
    distance, parent, candidate = heappop(queue)
    if candidate in parents: continue
    parents[candidate] = parent
    if candidate == target:
      return distance - heuristic(target), parents
    for neighbor in graph[candidate]:
      weight = graph[candidate][neighbor] - heuristic(candidate) + heuristic(neighbor)
      heappush(queue, (distance + weight, candidate, neighbor))
  return inf, None


class WordNeighbors(object):

  def __init__(self, words):
    self.words = words
    self.M = dict()                 # Neighbor words

  def variants(self, wd, words):    # Yield all word variants
    wasl = list(wd)                 # Convert word to a list
    for i, c in enumerate(wasl):    # Each position and character
      for oc in chars:              # Every possible character
        if c == oc: continue        # Skip the same character
        wasl[i] = oc                # Replace the character
        ow = ''.join(wasl)          # Make a string of the word
        if ow in words:             # Is it a valid word?
          yield ow                  # Yield it
      wasl[i] = c                   # Reset the character


  def __getitem__(self, wd):
    if wd not in self.M:
    # Cache the direct neighbors
      self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
    return self.M[wd]


  def heuristic(self, u, v):
    return sum(a!=b for a, b in zip(u, v))


  def ladder(self, s, t, h=None):
    if h is None:
      def h(v):
        return self.heuristic(v, t)

    _, P = a_star(self, s, t, h)
    if P is None:
      return [s, None, t]

    u, p = t, []
    while u is not None:            # Get path to target
      p.append(u)
      u = P[u]

    p.reverse()                     # The path is backward
    return p


if __name__ == '__main__':
  wds = set(line.strip().lower() for line in open("/usr/share/dict/words"))
  G = WordNeighbors(wds)
  print G.ladder('lead', 'gold')
  print G.ladder('teamwork', 'vacation')
  print G.ladder('axe', 'pie')
  print G.ladder('axe', 'pie', h = lambda v: 0)
  print counter, G.ladder('camera', 'harder')
  print counter, G.ladder('camera', 'harder', h = lambda v: 0)
