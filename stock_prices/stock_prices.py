#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit_so_far = float('-inf')
  for i in range(0, len(prices)):
    for j in range(0, len(prices)):
      if i >= j:
        pass
      elif (prices[j] - prices[i] > max_profit_so_far):
        max_profit_so_far = prices[j] - prices[i]
  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))