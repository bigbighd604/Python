#!/usr/bin/env python


from heapq import heappush, heappop
from string import ascii_lowercase as chars


inf = float('inf')

def a_star(G, s, t, h):
  P, Q = {}, [(h(s), None, s)]
  while Q:
    d, p, u = heappop(Q)
    if u in P: continue
    P[u] = p
    if u == t: return d - h(t), P
    for v in G[u]:
      w = G[u][v] - h(u) + h(v)
      heappush(Q, (d + w, u, v))
  return inf, None

class WordSpace(object):

  # An implicit graph w/utils
  def __init__(self, words): # Create graph over the words
    self.words = words
    self.M = dict()

  def variants(self, wd, words): #
    wasl = list(wd) #
    for i, c in enumerate(wasl): #
      for oc in chars: #
        if c == oc: continue #
        wasl[i] = oc #
        ow = ''.join(wasl) #
        if ow in words: #
          yield ow #
      wasl[i] = c #

  def __getitem__(self, wd):
    # The adjacency map interface
    if wd not in self.M:
    # Cache the neighbors
      self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
    return self.M[wd]

  def heuristic(self, u, v): # The default heuristic
    return sum(a!=b for a, b in zip(u, v)) # How many characters differ?

  def ladder(self, s, t, h=None): # Utility wrapper for a_star
    if h is None: # Allows other heuristics
      def h(v): 
        return self.heuristic(v, t) 

    _, P = a_star(self, s, t, h) 
    if P is None: 
      return [s, None, t] 

    u, p = t, [] 
    while u is not None: 
      p.append(u) 
      u = P[u] 

    p.reverse() 
    return p 


if __name__ == '__main__':
  wds = set(line.strip().lower() for line in open("/usr/share/dict/words"))
  G = WordSpace(wds)
  print G.ladder('lead', 'gold')
  print G.ladder('cold', 'wats')
