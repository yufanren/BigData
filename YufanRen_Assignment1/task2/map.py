#!/usr/bin/env python
import sys

def QuotationFix(s):
  new_s, i = [], 0
  while i < len(s):
    if '"' in s[i]:
      item = s[i]
      counter = i
      i += 1
      while counter < len(s) - 1 and '"' not in s[counter + 1]:
        counter += 1
      for j in range (i, min(counter + 2, len(s))):
        item += ',' + s[j]
      new_s.append(item.replace('"', ''))
      i = counter + 1
    else:
      new_s.append(s[i])
    i += 1
  return new_s

# split the lines into a pair
output = {}
for line in sys.stdin:
  info = line.strip().split(',')
  if '"' in line:
    info = QuotationFix(info)
  if len(info) == 22:
    if info[0] == 'summons_number':
      continue
    #key is "violation_code"
    key = info[2]
    if key in output:
      output[key] += 1
    else:
      output[key] = 1
for key in output.keys():
  print '%s\t%d' % (key, output[key])

