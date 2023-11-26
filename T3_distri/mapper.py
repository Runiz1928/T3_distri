#!/usr/bin/env python3

import sys 

for line in sys.stdin: 
    line = line.strip().lower()
    words = line.split()
    for word in words: 
        print('{}\t{}'.format(word, 1))
