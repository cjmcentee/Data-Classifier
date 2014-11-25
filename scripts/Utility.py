__author__ = 'coltonmcentee'

from operator import sub
from math import sqrt, pow

def distance(point1, point2):
    difference = tuple(map(sub, point1, point2))
    norm = 0
    for coordinate in difference:
        norm += pow(coordinate, 2)

    dist = sqrt(norm)
    return dist

def average_point(points):
    added = tuple([sum(p) for p in zip(*points)])
    avg = tuple(map(lambda e: e / len(points), added))
    return avg