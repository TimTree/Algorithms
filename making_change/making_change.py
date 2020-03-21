#!/usr/bin/python

import sys

'''
1 (1)
  1 penny
2 (2)
  1 doublecent
  2 pennies
3 (2)
  1 doublecent and 1 penny
  3 pennies
4 (3)
  2 doublecents
  1 doublecent and 2 pennies
  4 pennies
5 (4)
  1 nickel
  2 doublecents and 1 penny
  2 doublecents and 3 pennies
  4 pennies
6 (5)
  1 nickel and 1 penny
  3 doublecents
  2 doublecents and 2 pennies
  1 doublecent and 4 pennies
  6 pennies
7 (6)
  1 nickel and 1 doublecent
  1 nickel and 2 pennies
  3 doublecents and 1 penny
  2 doublecents and 3 pennies
  1 doublecent and 5 pennies
  7 pennies
8 (7)
  1 nickel, 1 doublecent, and 1 penny
  1 nickel and 3 pennies
  4 doublecents
  3 doublecents and 2 pennies
  2 doublecents and 4 pennies
  1 doublecent and 6 pennies
  8 pennies
9 (8)
  1 nickel and 2 doublecents
  1 nickel, 1 doublecent, and 2 pennies
  1 nickel and 4 pennies
  4 doublecents and 1 penny
  3 doublecents and 3 pennies
  2 doublecents and 5 pennies
  1 doublecent and 7 pennies
  9 pennies
10 (10)
  2 nickels
  1 nickel, 2 doublecents, and 1 penny
  1 nickel, 1 doublecent, and 3 pennies
  1 nickel and 5 pennies
  5 doublecents
  4 doublecents and 2 pennies
  3 doublecents and 4 pennies
  2 doublecents and 6 pennies
  1 doublecent and 8 pennies
  10 pennies
'''
def making_change(amount, denominations):
    # Cache is the running total of combination of coins based on cents
    # cache[0] is the total amount of combinations for 0 cents
    # cache[1] is for 1 cent
    cache = [0] * (amount + 1)
    cache[0] = 1
    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            cache[higher_amount] += cache[higher_amount - coin]
    return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")


making_change(10, [1, 5, 10, 25, 50])