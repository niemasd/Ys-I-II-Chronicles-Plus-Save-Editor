#!/usr/bin/env python3
'''
Print a summary about a given Ys I & II Chronicles+ save file
'''

# imports
from sys import argv
from ys_chronicles_save import Save

# main program
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s ys#_#.bmp" % argv[0]); exit(1)
    save = Save(argv[1])
    save.print_summary()