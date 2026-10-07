MAX_TS = 100
CALORIES = 500

def getValue(ingredients, recipe):
    ing_names = list(ingredients.keys())
    capacity = durability = flavor = texture = 0
    for i in range(0, len(recipe)):
        capacity += ingredients[ing_names[i]][0] * recipe[i]
        durability += ingredients[ing_names[i]][1] * recipe[i]
        flavor += ingredients[ing_names[i]][2] * recipe[i]
        texture += ingredients[ing_names[i]][3] * recipe[i]

    capacity = 0 if capacity < 0 else capacity
    durability = 0 if durability < 0 else durability
    flavor = 0 if flavor < 0 else flavor
    texture = 0 if texture < 0 else texture

    return capacity * durability * flavor * texture

def getBestOptionWithCalories(ing_names, ingredients, current, current_calories, best_value, best_recipe):
    rest_ts = MAX_TS - sum(current)
    if len(ing_names) == 1: 
        aux = current.copy()
        aux.append(rest_ts)
        aux_calories = current_calories + ingredients[ing_names[0]][4] * rest_ts
        if aux_calories == CALORIES:
            current_value = getValue(ingredients, aux)
            if current_value > best_value:
                return (aux, current_value)
            else:
                return None # it is not better
        else:
            return None # calories not exact
    else:
        new_best_value = best_value
        new_best_recipe = best_recipe.copy()
        better_found = False
        for ts in range(0, rest_ts + 1):
            aux = current.copy()
            aux.append(ts)
            aux_calories = current_calories + ingredients[ing_names[0]][4] * ts
            if aux_calories <= CALORIES:
                res = getBestOptionWithCalories(ing_names[1:], ingredients, aux, aux_calories,new_best_value, new_best_recipe)
                if res != None: # there is one better
                    better_found = True
                    new_best_recipe = res[0].copy()
                    new_best_value = res[1]

        if better_found:
            return (new_best_recipe, new_best_value)
        else: 
            return None
   

def getBestOption(ing_names, ingredients, current, best_value, best_recipe):
    rest_ts = MAX_TS - sum(current)
    if len(ing_names) == 1: 
        aux = current.copy()
        aux.append(rest_ts)
        current_value = getValue(ingredients, aux)
        if current_value > best_value:
            return (aux, current_value)
        else:
            return None # it is not better
    else:
        new_best_value = best_value
        new_best_recipe = best_recipe.copy()
        better_found = False
        for ts in range(0, rest_ts + 1):
            aux = current.copy()
            aux.append(ts)
            res = getBestOption(ing_names[1:], ingredients, aux, new_best_value, new_best_recipe)
            if res != None: # there is one better
                better_found = True
                new_best_recipe = res[0].copy()
                new_best_value = res[1]

        if better_found:
            return (new_best_recipe, new_best_value)
        else: 
            return None

def number15_1():
    dataFile = open("data/day15.txt", "r")

    ingredients = dict()
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        s_line = s_line.replace(":", "")
        s_line = s_line.replace(",", "")

        v_line = s_line.split(" ")
        ingredients[v_line[0]] = [int(v_line[2]), int(v_line[4]), int(v_line[6]), int(v_line[8]), int(v_line[10])] # capacity, durability, flavor, texture and calories

    (recipe, value) = getBestOption(list(ingredients.keys()), ingredients, [], -1, [])

    print("Result Day 15 Part 1: " + str(value))

def number15_2():
    dataFile = open("data/day15.txt", "r")

    ingredients = dict()
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        s_line = s_line.replace(":", "")
        s_line = s_line.replace(",", "")

        v_line = s_line.split(" ")
        ingredients[v_line[0]] = [int(v_line[2]), int(v_line[4]), int(v_line[6]), int(v_line[8]), int(v_line[10])] # capacity, durability, flavor, texture and calories

    (recipe, value) = getBestOptionWithCalories(list(ingredients.keys()), ingredients, [], 0, -1, [])

    print("Result Day 15 Part 2: " + str(value))

number15_1()
number15_2()