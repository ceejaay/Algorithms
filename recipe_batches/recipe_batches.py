#!/usr/bin/python
rec = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
ing = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
import math

# print(list(ing))

def recipe_batches(recipe, ingredients):
    # if teh recipe key is not in ingredients return 0
    for i in recipe:
        if i not in ingredients:
            return False
        else:
            return True


    # diff = recipe.keys() - ingredients.keys()
    # diff =  ''.join(diff)

    # # print(diff)
    # if diff in ingredients:
    #     print(True)

    # for key in recipe: 
    #     if key not in ingredients.keys()


# return list(recipe) == list(ingredients)


print(recipe_batches(rec, ing))
# 1. check for matching keys.
  # a. we have to check for the keys from the rec if they are included in the ingredients. 
  # b. Ingredients has to match the recipe. You hvae to have all the keys from the indredients in the recipe.
# 2. check recpie amounts agains the ingredient amounts. 
#    ie: ingredients amount // recipe amount
# 3. If any come back with zero. Return zero.
# 4. If All come back with 1. return 1
# 5. If all come back the same number. Return that number
# 6. if they all have different numbers. Then return the lowest number.

# We look at the recipies. Check the keys. If they  all exist in the ingredients then we can go a head.
# other wise return 0

# We check each ingredient against each other. We do some division. with the // operator. If everthing is above 0 then we can make the thing. 

# If not, then we return 0




# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
