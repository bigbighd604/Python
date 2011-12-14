#!/usr/bin/env python
#
# Q. Maximum the number of flies the frog can eat
# Limitations: the frog can only move right or down
# Requirements:
# 1. Time complexity - O(n^2)
#
# i.e.
# -------------------------
# |frog |  2  |  0  |  1  |
# -------------------------
# |  1  |  3  |  0  |  2  |
# -------------------------
# |  2  |  1  |  1  |  2  |
# -------------------------
# |  3  |  2  |  3  |exit |
# -------------------------
#
# The above square can be any size.
#



weight=[[0,2,0,1],[1,3,0,2],[2,1,1,2],[3,2,3,0]]

def GetMaxFlies(weight):
  flies = {}
  for i in xrange(4):
    for j in xrange(4):
      if i == 0 and j == 0:
        flies[(i,j)] = 0
      elif i == 0:
        flies[(i,j)] = flies[(i, j - 1)] + weight[i][j]
      elif j == 0:
        flies[(i,j)] = flies[(i - 1, j)] + weight[i][j]
      else:
        flies[(i,j)] = max(flies[(i - 1, j)], flies[(i, j - 1)]) + weight[i][j]
  return flies[(3,3)]


def GetMaxFliesAndPath(weight):
  flies = {}
  path = {(0, 0): None}
  height = len(weight)
  width = len(weight[0])

  for i in xrange(height):
    for j in xrange(width):
      if i == 0 and j == 0:
        flies[(i,j)] = 0
      elif i == 0:
        flies[(i,j)] = flies[(i, j - 1)] + weight[i][j]
        path[(i, j)] = (i, j - 1)
      elif j == 0:
        flies[(i,j)] = flies[(i - 1, j)] + weight[i][j]
        path[(i, j)] = (i - 1, j)
      else:
        if flies[(i - 1, j)] > flies[(i, j - 1)]:
          flies[(i, j)] = flies[(i - 1, j)] + weight[i][j]
          path[(i, j)] = (i - 1, j)
#        elif flies[(i - 1, j)] < flies[(i, j - 1)]:
        else:
          flies[(i, j)] = flies[(i, j - 1)] + weight[i][j]
          path[(i, j)] = (i, j - 1)
##        else:
##          flies[(i, j)] = flies[(i - 1, j)] + weight[i][j]
##          top_parent = path[(i - 1, j)]
##          left_parent = path[(i, j - 1)]
##          while (top_parent != None and left_parent != None):
##            if flies[top_parent] > flies[left_parent]:
##              path[(i, j)] = (i - 1, j)
##              break
##            else:
##              path[(i, j)] = (i, j - 1)
##              break
##            top_parent = path[top_parent]
##            left_parent = path[left_parent]

  return flies[(height - 1, width - 1)], path


if __name__ == "__main__":
  print 'Board is:'
  for line in weight:
    print line
  max_flies = GetMaxFlies(weight)
  print 'Max flies number is: %s' % max_flies
  max_flies, path = GetMaxFliesAndPath(weight)
  print max_flies
  height = len(weight)
  width = len(weight[0])

  print '(%s, %s) -> ' % (height -1, width - 1),
  parent = path[(height - 1, width - 1)]
  while (parent != None):
    print '(%s, %s) -> ' % parent,
    parent = path[parent]
  print 'None'
