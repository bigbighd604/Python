#!/usr/bin/env python

from string import ascii_lowercase as chars

def DiffOneLetter(wd, words): #
  wasl = list(wd) #
  for i, c in enumerate(wasl): #
    for oc in chars: #
      if c == oc: continue #
      wasl[i] = oc #
      ow = ''.join(wasl) #
      if ow in words: #
        yield ow #
    wasl[i] = c #


if __name__ == '__main__':
  wds = set(line.strip().lower() for line in open("/usr/share/dict/words"))
  print list(DiffOneLetter('cat', wds))
  print list(DiffOneLetter('stack', wds))
