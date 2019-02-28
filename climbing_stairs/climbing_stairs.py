#!/usr/bin/python

# We have 3 options when it comes to the hopping.
# 1 2, & 3.

# So for n.
# if we choose one of the above options, how many stairs are left?
#     if n = 3
#         if we pick 3 we have 0 stairs left. 3 - 3 = 0
#             if we pick 2 
#                 3 - 2 = 1
#             if we pick 1
#                 3 - 1 = 2

# if n = 0 then we know that we've reached the end.
# Subtract 1, 2, or 3. When we get to zero that is one combination.
# N
# if n - 1 == 0 then increment combo.
#     if it does not == zero then we have to check the difference. ie  n = 4 n - 2 == 0 So then we have to do climbing_stairs(n -2)



import sys

def climbing_stairs(n, cache=None):
    combos = 0
    if n <= 0:
        combos += 1
    else:
        climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)
        return combos
    # base case is n <= 0













print(climbing_stairs(5))


# 3 stairs.
# 1, 1, 1
# 2, 1
# 1, 2
# 3

# 4 stairs
# 1 1 1 1
# 1 3
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2
# 3 1




# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_stairs = int(sys.argv[1])
#     print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
#   else:
#     print('Usage: climbing_stairs.py [num_stairs]')


