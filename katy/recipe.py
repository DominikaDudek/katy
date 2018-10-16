def cakes(recipe, available):

    if available.keys() != recipe.keys():
        return 0

    how_many_cakes = {}
    for ingredient, amount in available.items():
        for recipe_ingr, recipe_amount in recipe.items():
            if ingredient == recipe_ingr:
                new_amount = amount // recipe_amount
                how_many_cakes[ingredient] = new_amount
                break

    return min(how_many_cakes.values())




a = cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})

print cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000})
