#!/usr/bin/python

import argparse

# base case would be an empty  array or a zero index
# The path to base case would be going down.


def find_max_profit(prices):
    # set index to length of array
    index = len(prices)
    # index is length of the price array
    # print(index)
    # we count down the array
    # while index > 1:
    # index = len(prices)
    # the highest should be waaaay less than zero since we'll get a lot of negative numbers
    highest = float('-inf')
    # we use the index to go backards
        # find_max_profit(prices[index:])
        # print(prices)
    # Then we go count down with the index
    while index > 0:
        # go forward in the array
        for i in range(index, len(prices)):
            # check which profit is higer. We get a lot of negatives
            if prices[i] - prices[index - 1] > highest:
                # set the new highest to the highest
                highest = prices[i] - prices[index -1]
                # de increment the index
        index -= 1
        # return the highest profit
    return highest
        # print('*********')
# find the min and the max.
# Can I buy?
# If I can't buy then I have to move on to the next min.
# for the first item we check them all.
#     the second item we check the array excluding the first.
#     the third item we check excluding the first and second
#     the foruth item we check excludint the 
print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([10, 7, 5, 8, 11, 9]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))
# So we want to look at the first price. 
# compare it to the later prices. See what the profit is for each one after the price.
# so you want to compare each price AFTER that price. Then return the one that is greatest.
# 1050
# 270 -1050 = -780
# 1540 - 1050 = 490
# 3800 - 1050 = 2750
# 2 - 1050 = -1048

# 270
# 1540 - 270 = 1270
# 3800 - 270 = 3530
# 2 - 270 = -268
# etc.

# We don't have to worry about the last price.
# Unless it's to subtract.
# We have an index to keep track of the highest.
# then we go throug and do the math for each one.
# If it's higher than the highest index, we set it to the newest number.
# jkkk




# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
