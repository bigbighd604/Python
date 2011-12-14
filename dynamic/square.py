#!/usr/bin/env python
#
# Q1. Given a array, request (a,b), give sum of [a:b]
# Requirements:
# 1. Time complexity -O(1)
# 2. Space complexity - O(1) # or no extra space
# 3. Data size - 10^7
#
# Q2. Given a n*n square, request ((a,b), (c,d)), give sum of sub square
# Requirements:
# 1. Time complexity -O(1)
# 2. Space complexity - O(1) # or no extra space
# 3. Data size - 10^7*10^7
#


def ArraySum(array):
  for i in xrange(1, len(array)):
    array[i] = array[i] + array[i-1]


def QuerySub(start, end):
  if start == 0:
    return array[end]
  else:
    return array[end] - array[start - 1]


def SquareSum(square):
  height = len(square)
  width = len(square[0])
  for i in xrange(height):
    for j in xrange(1, width):
      square[i][j] = square[i][j] + square[i][j-1]
    for j in xrange(width):
      if i == 0:
        break
      else:
        square[i][j] = square[i - 1][j] + square[i][j]


def QuerySubSquare(start, end):
  a, b = start
  d, c = end

  if a == 0 and b == 0:
    return square[d][c]
  elif a == 0:
    return square[d][c] - square[d][b - 1] + square[a][b - 1]
  elif b == 0:
    return square[d][c] - square[a - 1][c] + square[a - 1][b]
  else:
    return square[d][c] - square[a - 1][c] - square[d][b - 1] + square[a - 1][b - 1]

if __name__ == "__main__":
  array = [1,2,3,4,5,6,7,8,9,10]
  print array
  ArraySum(array)
  print array
  sum = QuerySub(2,5)
  print 'QuerySub(2,5) = %s' % sum
  sum = QuerySub(0,5)
  print 'QuerySub(0,5) = %s' % sum
  sum = QuerySub(0,9)
  print 'QuerySub(0,9) = %s' % sum

  square = [
      [1,2,3,4,5,6],
      [2,3,4,5,6,7],
      [3,4,5,6,7,8],
      [4,5,6,7,8,9],
      [5,6,7,8,9,0]]
  for line in square:
    print line
  SquareSum(square)
  for line in square:
    print line
  sum = QuerySubSquare((1, 1), (2, 3))
  print 'QuerySubSquare((1, 1), (2, 3)) = %s' % sum
  sum = QuerySubSquare((2, 1), (4, 3))
  print 'QuerySubSquare((2, 1), (4, 3)) = %s' % sum
  sum = QuerySubSquare((0, 0), (1, 1))
  print 'QuerySubSquare((0, 0), (1, 1)) = %s' % sum
  sum = QuerySubSquare((0, 0), (4, 5))
  print 'QuerySubSquare((0, 0), (5, 5)) = %s' % sum
  sum = QuerySubSquare((1, 0), (2, 3))
  print 'QuerySubSquare((1, 0), (2, 3)) = %s' % sum
  sum = QuerySubSquare((0, 1), (2, 3))
  print 'QuerySubSquare((0, 1), (2, 3)) = %s' % sum
