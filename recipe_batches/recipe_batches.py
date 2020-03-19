#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = float('inf')
  for x in recipe:
    try:
      if ingredients[x] // recipe[x] < max_batches:
        max_batches = ingredients[x] // recipe[x]
    except KeyError:
      return 0
  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))