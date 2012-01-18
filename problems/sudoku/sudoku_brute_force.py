#!/usr/bin/env python
#
# From http://mehpic.blogspot.com/2011/10/solve-any-sudoku-with-10-lines-of.html
#

input_board = [
  7,0,0,4,0,9,0,0,6,
  5,0,9,0,8,6,1,2,0,
  1,4,0,0,0,0,0,0,0,
  6,5,0,8,0,0,0,0,0,
  0,2,4,9,0,1,5,6,0,
  0,0,0,0,0,2,0,1,8,
  0,0,0,0,0,0,0,8,7,
  0,7,5,2,4,0,6,0,1,
  2,0,0,3,0,7,0,0,5
  ]

board_size = 9
subsquare_width = 3
subsquare_height = 3

def prettyprint(board, board_size):
  print
  for i in range(board_size):
    print board[i*board_size:i*board_size+board_size]


col_labels = [i%board_size for i in range(len(input_board))]
row_labels = [i/board_size for i in range(len(input_board))]
sqr_labels = [(board_size/subsquare_width)*(row_labels[i]/subsquare_height)+col_labels[i]/subsquare_width for i in range(len(input_board))]


def solve(board):
  try:
    i = board.index(0)
  except:
    prettyprint(board, board_size)
    return
  # find out numbers already used in same row, column or square.
  bag = [board[j] for j in filter(lambda x: (col_labels[i]==col_labels[x]) or (row_labels[i]==row_labels[x]) or (sqr_labels[i]==sqr_labels[x]),range(len(board)))]
  # get numbers can be used to put in a position
  for j in filter(lambda x: x not in bag, range(1,board_size+1)):
    # get one number, put in this position, call itself again.
    board[i] = j; solve(board); board[i] = 0

solve(input_board)
