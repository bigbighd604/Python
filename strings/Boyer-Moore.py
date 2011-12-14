#!/usr/bin/env python
#
#


def IsPrefix(string, position):
  """Test if the suffix of string starting from position is a prefix of string.
  Args:
    string: A literal string.
    position: A integer indicates the position.

  Returns:
    True if is a prefix, or False.
  """
  length = len(string)
  suffix_length = length - position
  counter = 0
  while (counter < suffix_length and
         string[counter] == string[position + counter]):
    counter += 1
  return not (counter < suffix_length)


def SuffixLength(str, pos):
  """length of the longest suffix of string ending on position.
  Args:
    string: A literal string.
    position: A integer indicates the position.

  Returns:
    A integer.
  """
  length = len(str)
  counter = 0
  # increment suffix length to the first mismatch or beginning of str.
  while (str[pos - counter] == str[length - 1 - counter]) and (counter < pos):
    counter += 1
  return counter


if __name__ == "__main__":
  str1 = "abcfefabcf"
  print IsPrefix(str1, 6)
  str2 = "dddbcabc"
  print SuffixLength(str2, 4)
