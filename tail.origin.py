#!/usr/bin/python

import os
import sys

NUM_LINES = 10

if __name__ == '__main__':

  with open(sys.argv[1]) as f:
    line_ends_seen = 0
    chunk_size = 4096
    remaining_bytes = os.stat(sys.argv[1]).st_size

    while remaining_bytes:
      if chunk_size < remaining_bytes:
        remaining_bytes -= chunk_size
      else:
        chunk_size = remaining_bytes
        remaining_bytes = 0
      f.seek(remaining_bytes);
      chunk = f.read(chunk_size);
      i = chunk_size
      while line_ends_seen <= NUM_LINES:
        i -= 1
        if i < 0: break
        if chunk[i] == '\n':
          line_ends_seen += 1
      if line_ends_seen > NUM_LINES: break
    #sys.stdout.write(chunk[i+1:])
    f.seek(remaining_bytes+i+1)
    while True:
      chunk = f.read(chunk_size)
      if chunk:
        sys.stdout.write(chunk)
      else:
        break
