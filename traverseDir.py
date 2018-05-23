#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

def recursive(path):
    dir = [x for x in os.listdir(path) if os.path.isdir(path + '/' + x)]
    for d in dir:
        print(path + '/' + d)
        recursive(path + '/' + d)

    return 0

inputPath = sys.argv[1]
if os.path.isdir(inputPath):
    recursive(inputPath)
else:
    print("The input path must be a directory.")