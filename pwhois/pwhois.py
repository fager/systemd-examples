#!/usr/bin/env python

import sys
import select


searchterms = None

if select.select([sys.stdin,],[],[],0.0)[0]:
    searchterms = sys.stdin.readline().split()


if searchterms != None:
  print("; ","PWhois System Information Server v0.1")
  print()

  if 'Frank' in searchterms:
    print("name:","Frank Agerholm")
    print("role:","System Administrator")
    print()


