#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    pass
    # So for every stair the kid touches. She can do it three different ways.

    # The kid can touch every stair once. 
    # or The kid can touch every other stair.
    # Or every third stair.
    # But if the kid hops three stairs,

    # Every stair except the top 3 and bottom 3 has can be reached by 1 2 or 3 hops.
    # Two can only be reached by one hop.
    # Top stair.
    # 5 stairs.
    # Stair 1.
    #     jump to the

    # for every stair we need to calculate down to 0 from 3.o
    #     for every step. We increment by both 1 2, & 3 unless you are the bottom steps.

# for each number we have to calculate the steps.
    # keeping in mind the end and beginning of the stairs.

    # number + 3
    # number + 2
    # number + 1
    # Starting a the top.
    # The possible number combinations requried to reach the stair is this.
    # 9 
    # the steps are 

# def fib(n):
#     count = 0
#     if n <= 0:
#         return "enter a positive number"
#     elif n == 1:
#         return 0
#     else:
#         while count < n
#             return













  # pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
