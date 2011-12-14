'''
Created on Oct 17, 2011

@author: bighead
'''

import random
import time

import algorithms


def GenerateList(size = 100):
  data = [ random.randint(0, 50000) for i in range(size) ]
  return data


def TimeWorker(algorithm, data_size):
    data = GenerateList(data_size)
    start_time = time.clock() # Returns floating point number of seconds
    result = getattr(algorithms, algorithm)(data)
    stop_time = time.clock()
    return (stop_time - start_time, result)


def TimeAlgorithm(algorithms = None, min_size = 0, max_size = 100000,
                  step = 500, enable_threshold = False, threshold = 20,
                  print_result = False):
  all_time_list = []
  all_number_list = []
  if algorithms:
    algorithms_status = {}
    for algorithm in algorithms:
      algorithms_status[algorithm] = [True, None]

    for size in range(min_size, max_size, step):
      time_list = []
      number_list = []
      for algorithm in algorithms:
        if enable_threshold and algorithms_status[algorithm][0]:
          process_time, result = TimeWorker(algorithm, size)
          if process_time >= threshold:
            algorithms_status[algorithm] = (False, process_time)
            print('Algorithm: %s stops running due to exceed threshold time: %s' % (algorithm, threshold))
        elif enable_threshold:
          process_time = algorithms_status[algorithm][1]
        else:
          process_time, result = TimeWorker(algorithm, size)
        print('[Algorithm: %s, Data Size: %s, Process Time: %s' % (algorithm, size, process_time))
        time_list.append(process_time)
        number_list.append(size)
        if print_result:
          print(result)
      all_time_list.append(time_list)
      all_number_list.append(number_list)
  return (all_number_list, all_time_list)
