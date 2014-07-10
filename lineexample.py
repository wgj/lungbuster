#! /usr/bin/python
import sys

n = 0

for i in xrange(1000000):
  n = i
  sys.stdout.write('iterations: %d \r' % n)
  sys.stdout.flush()
