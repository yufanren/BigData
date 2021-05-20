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

for line in sys.stdin:
  info = line.strip().split(',')
  if '"' in line:
    info = QuotationFix(info)
  if len(info) != 22 or info[0] == 'summons_number':
    continue
  if not info[20]:
    info[20] = 'NONE'
  key = 'a' + ',' + info[20]
  print '%s\t%d' % (key, 1)
  if not info[19]:
    info[19] = 'NONE'
  key = 'b' + ',' + info[19]
  print '%s\t%d' % (key, 1)
