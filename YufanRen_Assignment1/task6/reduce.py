#!/usr/bin/env python
import sys
import string
from Queue import PriorityQueue

curr_key = None
curr_count = 0
curr_max = PriorityQueue()

#Place all outputs in a size 20 priority queue
for line in sys.stdin:
  key, value = line.strip().split('\t', 1)
  if key == curr_key:
    curr_count += int(value)
  else:
    curr_max.put((curr_count, curr_key))
    while curr_max.qsize() > 20:
      curr_max.get()
    curr_key = key
    curr_count = int(value)
curr_max.put((curr_count, curr_key))
while curr_max.qsize() > 20:
  curr_max.get()
high_list = []
while curr_max.qsize() > 0:
  high_list.append(curr_max.get())
high_list.sort(key=lambda x:x[0], reverse=True)
for pair in high_list:
  print '%s\t%d' % (pair[1], pair[0])