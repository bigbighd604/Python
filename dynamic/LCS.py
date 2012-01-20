#!/usr/bin/env python

# Longest Common Sequence, my not contigous

import sys

def LCS(str1, str2):
  row_num = len(str1) + 1
  col_num = len(str2) + 1

  # 2 dimension array to store LCS until a position
  # c[0] is all 0, c[x][0] is all 0
  c = [[0 for x in xrange(col_num)] for y in xrange(row_num)]

  # 2 dimension array to store the path to a LCS
  b = [[(0, 0) for x in xrange(col_num)] for y in xrange(row_num)]

  # Calculate all common sequences
  for i in xrange(1, row_num):
    for j in xrange(1, col_num):
      if str1[i - 1] == str2[j - 1]:
        c[i][j] = c[i - 1][j - 1] + 1
        b[i][j] = (i - 1, j - 1)
      else:
        if c[i - 1][j] >= c[i][j - 1]:
          c[i][j] = c[i - 1][j]
          b[i][j] = (i - 1, j)
        else:
          c[i][j] = c[i][j - 1]
          b[i][j] = (i, j - 1)

  # Get the longest one
  length = c[row_num - 1][col_num - 1]
  string = ''
  row = row_num - 1
  col = col_num -1

  while row > 0 or col > 0:
    new_row, new_col = b[row][col]
    if c[row][col] != c[new_row][new_col]:
      string += str1[row - 1]
    row = new_row
    col = new_col

  return length, string[::-1]


if __name__ == '__main__':
  str1 = sys.argv[1]
  str2 = sys.argv[2]
  length, string= LCS(str1, str2)
  print length, string
