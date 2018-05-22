#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import argparse

helpContent="The path which you want to traverse.\n" \
            "The absolute path and relative path are accepted.\n" \
            "EX: /datacenter/MDATA or MDATA\n"
parser = argparse.ArgumentParser()
parser.add_argument("-p", dest="path", help="The path which you want to traverse.", required=True)
option = parser.parse_args()

def recursive(path):
    dir = [x for x in os.listdir(path) if os.path.isdir(path + '/' + x)]
    for d in dir:
        print(path + '/' + d)
        recursive(path + '/' + d)

    return 0

inputPath = option.path
recursive(inputPath)