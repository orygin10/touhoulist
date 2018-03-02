#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

with open('touhoulist.txt', 'r') as f:
	charlist = f.read().splitlines()

r = int((ord(os.urandom(1)) / 255.0) * len(charlist)) - 1

print r
print charlist[r]