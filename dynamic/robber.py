#!/usr/bin/env python
#
# Q. A robber in a jewelry shop, he can only carry 7 pounds items
#    Each valuable item has a value and weight, (value, weight)
#    How could he maximum the value of items he will carry?
#
# i.e.
#
# items: (5, 2), (7, 3), (4, 2), (3, 4).
#


INFINITY = -100000

def GetMax(items, weight):
  l = (weight + 1) * [INFINITY]
  l[0] = 0
  max_cost = []
  for cost, weigh in items:
    nl = l[:]
    for i in xrange(weight + 1):
      if l[i] > INFINITY and i + weigh <= weight:
        new_cost = l[i] + cost
        if nl[i + weigh] < new_cost:
          nl[i + weigh] = new_cost
    max_cost.append(nl)
    l = nl
  return max_cost


def GetMaxWithPath(items, weight):
  l = []
  for i in xrange(weight + 1):
    l.append([INFINITY, []])
  l[0][0] = 0
  max_cost = []
  items_index = 0
  for cost, weigh in items:
    nl = l[:]
    for i in xrange(weight + 1):
      if l[i][0] > INFINITY and i + weigh <= weight:
        new_cost = l[i][0] + cost
        if nl[i + weigh][0] < new_cost:
          nl[i + weigh][1].append((cost, weigh))
    max_cost.append(nl)
    l = nl
  return max_cost


if __name__ == "__main__":
  items = [(5, 2), (7, 3), (4, 2), (3, 4)]
  weight = 7
  max_cost = GetMaxWithPath(items, weight)
  for line in max_cost:
    print line
