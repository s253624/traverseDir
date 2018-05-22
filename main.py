#!/usr/bin/python3

from pathlib import Path

def main():
    recursive('.')
    return 0

def recursive(path):
    p = Path(path)
    dir = [x for x in p.iterdir() if x.is_dir()]
    for d in dir:
        print(d)
        recursive(d)

    return 0

main()