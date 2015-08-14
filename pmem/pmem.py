#!/usr/bin/env python3

import sys

try:
  m1 = "F" * (1024*1024)
  m256 = m1 * 256
except MemoryError as e:
  print("Oh oh")
  sys.exit()

try:
  while True:
    pass
except KeyboardInterrupt as e:
  print("Bye bye")


