#! /usr/bin/python
import time
import sys

for i in xrange(10, 0, -1):
  n = i
  while n >= 0:
    sys.stdout.write('Breath for %d seconds.  \r' % n)
    time.sleep(1)
    sys.stdout.flush()
    n -= 1

  n = i
  while n >=0:
    sys.stdout.write('Exhale for %d seconds.  \r' % n)
    time.sleep(1)
    sys.stdout.flush()
    n -= 1
