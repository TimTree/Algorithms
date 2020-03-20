#!/usr/bin/python

import sys

combinations = ['rock', 'paper', 'scissors']
all_combinations = [['rock'], ['paper'], ['scissors']]

def rock_paper_scissors(n):
  if n < 1:
    return []
  elif n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    #all_combinations_backup = all_combinations.copy()
    #all_combinations.extend(all_combinations)
    #all_combinations.extend(all_combinations_backup)
    #print(all_combinations)
    #for i in all_combinations:
    #  i.append('s')
    #  print(all_combinations)
    #return rock_paper_scissors(n-1)
    for _ in range(1, n):
      all_combinations_backup = all_combinations.copy()
      for i in range(0,len(all_combinations)):
        all_combinations.append(all_combinations[i])
      print(all_combinations[0])
      all_combinations[0].append('rock')
    return all_combinations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')