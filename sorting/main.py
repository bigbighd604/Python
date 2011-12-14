'''
Created on Oct 17, 2011

@author: bighead
'''

import csv
import time
import matplotlib.pyplot as plt

import common


def main():
  algorithm_list = ('BubbleSort', 'SelectionSort', 'InsertionSort',
                    'QuickSort', 'MergeSort', 'CountingSortWrapper',
                    'RadixSort', 'HeapSortWrapper')
  #algorithm_list = ('QuickSort', 'MergeSort', 'CountingSortWrapper', 'HeapSortWrapper')
  number_list, time_list = common.TimeAlgorithm(algorithm_list,
                                                max_size = 500000,
                                                step = 1000,
                                                enable_threshold = True)
  file_name = '%s' % time.strftime('%Y-%m-%d.%H:%M:%S')
  plt.figlegend(plt.plot(number_list, time_list), algorithm_list, 'upper left')
  plt.savefig('%s.pdf' % file_name)
  csv_writer = csv.writer(open('%s.csv' % file_name, 'wb'), delimiter = ',')
  csv_writer.writenow(["Title"] + number_list)
  for i in range(len(algorithm_list)):
    time_data = [item[i] for item in time_list]
    csv_writer.writenow([algorithm_list[i]] + time_data)


if __name__ == "__main__":
  main()
