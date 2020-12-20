"""
This script scrapes files from GitHub with specific algorithm purposes, and
labels them by the algorithm

Labels are:
    bubblesort
    mergesort
    quicksort
    linkedlist
    bfs (breadth first search)
    knapsack
"""

import pickle

from poj_cparser import read_oj_scripts
from java_parser import read_java_json

def ast4poj(infile, outfile):
    print('Load poj data')
    data = read_oj_scripts(infile)

    print('Dumping scripts')
    with open(outfile, 'wb') as file_handler:
        pickle.dump(data, file_handler, -1)

def ast4java(infile, outfile):
    print('Load java data')
    data = read_java_json(infile)

    print('Dumping scripts')
    with open(outfile, 'wb') as file_handler:
        pickle.dump(data, file_handler, -1)