#!/usr/bin/env python
import sys
import string

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
for line in sys.stdin:
  info = line.strip().split(',')
  if '"' in line:
    info = QuotationFix(info)
  if len(info) != 18 or info[0] == 'summons_number' or not info[12]:
    continue
  #key is 'license_type'
  key = info[2]
  amount = info[12]
  print '%s\t%s' % (key, amount)

