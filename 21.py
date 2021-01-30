import sys


def extra():
    fp = open("21.input")
    food = []

    all_ingredients = set()
    all_allergens = set()
    for line in fp.readlines():
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        ingredients, allergens = line.strip().split('contains')
        ingredients = ingredients.strip().split()
        allergens = allergens.strip().split()

        for ingredient in ingredients:
            all_ingredients.add(ingredient)

        for allergen in allergens:
            all_allergens.add(allergen)

        food.append((ingredients, allergens))

    # print(all_ingredients, len(all_ingredients))
    # print(all_allergens, len(all_allergens))

    food_with_allergen = dict((x, []) for x in all_allergens)
    for idx, (ingredients, allergens) in enumerate(food):
        for allergen in allergens:
            food_with_allergen[allergen].append(idx)

    ingredient_with_allergen = {}
    for allergen in all_allergens:
        ingredient_with_allergen[allergen] = food[food_with_allergen[allergen]
                                                  [0]][0]

        for food_id in food_with_allergen[allergen][1:]:
            tmp = set(food[food_id][0])
            ingredient_with_allergen[allergen] = list(
                set(ingredient_with_allergen[allergen]) & tmp)

    mapping = {}

    def search(idx, curr_mapping, mapping):

        if idx == len(all_allergens):
            xx = curr_mapping
            for val in curr_mapping:
                mapping[val] = curr_mapping[val]
            return

        allergen = list(all_allergens)[idx]
        for ingredient in ingredient_with_allergen[allergen]:
            if ingredient in curr_mapping:
                continue

            curr_mapping[ingredient] = allergen
            search(idx + 1, curr_mapping, mapping)
            del curr_mapping[ingredient]

    search(0, {}, mapping)

    ans = ','.join(sorted(mapping, key=lambda x: mapping[x]))
    print(ans)


def main():
    fp = open("21.input")
    food = []

    all_ingredients = set()
    all_allergens = set()
    for line in fp.readlines():
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        ingredients, allergens = line.strip().split('contains')
        ingredients = ingredients.strip().split()
        allergens = allergens.strip().split()

        for ingredient in ingredients:
            all_ingredients.add(ingredient)

        for allergen in allergens:
            all_allergens.add(allergen)

        food.append((ingredients, allergens))

    # print(all_ingredients, len(all_ingredients))
    # print(all_allergens, len(all_allergens))

    food_with_allergen = dict((x, []) for x in all_allergens)
    for idx, (ingredients, allergens) in enumerate(food):
        for allergen in allergens:
            food_with_allergen[allergen].append(idx)

    ingredient_with_allergen = {}
    for allergen in all_allergens:
        ingredient_with_allergen[allergen] = food[food_with_allergen[allergen]
                                                  [0]][0]

        for food_id in food_with_allergen[allergen][1:]:
            tmp = set(food[food_id][0])
            ingredient_with_allergen[allergen] = list(
                set(ingredient_with_allergen[allergen]) & tmp)

    mapping = {}

    def search(idx, curr_mapping, mapping):

        if idx == len(all_allergens):
            xx = curr_mapping
            for val in curr_mapping:
                mapping[val] = curr_mapping[val]
            return

        allergen = list(all_allergens)[idx]
        for ingredient in ingredient_with_allergen[allergen]:
            if ingredient in curr_mapping:
                continue

            curr_mapping[ingredient] = allergen
            search(idx + 1, curr_mapping, mapping)
            del curr_mapping[ingredient]

    search(0, {}, mapping)

    ans = 0
    for idx, (ingredients, allergens) in enumerate(food):
        for ingredient in ingredients:
            if ingredient in mapping:
                continue
            ans += 1
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()
