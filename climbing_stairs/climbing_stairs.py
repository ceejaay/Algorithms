#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    # So for every stair the kid touches. She can do it three different ways.

    # The kid can touch every stair once. 
    # or The kid can touch every other stair.
    # Or every third stair.
    # But if the kid hops three stairs,

    Every stair except the top 3 and bottom 3 has can be reached by 1 2 or 3 hops.
    Two can only be reached by one hop.
    Top stair.
    5 stairs.
    Stair 1.
        jump to the









  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
