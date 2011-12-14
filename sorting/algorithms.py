'''
Created on Oct 17, 2011

@author: bighead
'''

def BubbleSort(data):
  length = len(data)
  if length <= 1:
    return data
  for i in range(length - 1):
    for j in range(length - i - 1):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
  return data


def SelectionSort(data):
  length = len(data)
  if length <= 1:
    return data

  for i in range(length - 1):
    min_value = data[i]
    min_index = i
    for j in range(i + 1, length):
      if min_value > data[j]:
        min_value = data[j]
        min_index = j
    if min_index != i:
      data[min_index] = data[i]
      data[i] = min_value
  return data


def InsertionSort(data):
  length = len(data)
  if length <= 1:
    return data

  for i in range(1, length):
    item = data[i]
    for j in range(i):
      if item < data[i - j - 1]:
        data[i - j] = data[i - j - 1]
        data[i - j - 1] = item
      else:
        break
  return data


def QuickSort(data):
  length = len(data)
  if length <= 1:
    return data
  pivot_index = length / 2
  pivot = data[pivot_index]
  left = []
  right = []
  for item in data[:pivot_index] + data[pivot_index  + 1:]:
    if item <= pivot:
      left.append(item)
    else:
      right.append(item)

  return QuickSort(left) + [pivot] + QuickSort(right)


def MergeList(a, b):
  while a or b:
    if not a:
      yield b.pop(0)
    elif not b:
      yield a.pop(0)
    elif a[0] < b[0]:
      yield a.pop(0)
    else:
      yield b.pop(0)


def MergeSort(data):
  length = len(data)
  if length <= 1:
    return data

  return list(MergeList(MergeSort(data[:length / 2]), MergeSort(data[length / 2:])))


def CountingSort(data):
  assert all(0 <= x <= 50000 for x in data)
  counter = [0] * 50001
  for item in data:
    counter[item] += 1
  for x, count in enumerate(counter):
    for i in range(count):
      yield x


def CountingSortWrapper(data):
  return list(CountingSort(data))


def Digit(x, k):
  return (x / (10 ** k)) % 10


def SortByDigit(data, k):
  buckets = [[] for i in range(10)]
  for x in data:
    buckets[Digit(x, k)].append(x)
  for b in buckets:
    for x in b:
      yield x


def RadixSort(data, digit = 5):
  for k in range(digit):
    data = SortByDigit(data, k)
  return list(data)

class Heap(list):
  def FindMin(self):
    return self[0]

  def Parent(self, i):
    return (i - 1) / 2

  def Children(self, i):
    return i * 2 + 1, i * 2 + 2

  def Insert(self, e):
    self.append(e)
    i = len(self) - 1
    while i > 0:
      p = self.Parent(i)
      if self[p] > self[i]:
        self[p], self[i] = self[i], self[p]
        i = p
      else:
        return

  def DeleteMin(self):
    minimal = self[0]
    n = len(self) - 1
    self[0] = self[n]
    del self[n]

    i = 0
    while True:
      left, right = self.Children(i)
      if right < n and self[right] < self[left]:
        child = right
      elif left < n:
        child = left
      else:
        return minimal
      if self[child] < self[i]:
        self[i], self[child] = self[child], self[i]
        i = child
      else:
        return minimal


def HeapSort(data):
  heap = Heap()
  for element in data:
    heap.Insert(element)
  while heap:
    yield heap.DeleteMin()

def HeapSortWrapper(data):
  return list(HeapSort(data))
