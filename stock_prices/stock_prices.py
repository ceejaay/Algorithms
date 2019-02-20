#!/usr/bin/python

import argparse

def find_max_profit(prices):
    index = len(prices)
    highest = -999999999999
    while index >0:
        for i in range(index, len(prices)):
            if prices[i] - prices[index - 1] > highest:
                highest = prices[i] - prices[index -1]
            # print(f"{prices[i] - prices[index - 1]}")
        index -= 1
        # print('*********')




    return highest


# for the first item we check them all.
#     the second item we check the array excluding the first.
#     the third item we check excluding the first and second
#     the foruth item we check excludint the 
print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))
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
