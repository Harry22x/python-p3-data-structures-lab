spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    name = [food["name"] for food in spicy_foods]
    return name

def get_spiciest_foods(spicy_foods):
    pass
    name = [food for food in spicy_foods if food["heat_level"]>5]
    return name

def print_spicy_foods(spicy_foods):
    pass
    for x in spicy_foods:
        print(f"{x['name']} ({x['cuisine']}) | Heat Level: { '🌶' * x['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for food in spicy_foods:
        if(food["cuisine"] == cuisine):
            return food
    

def print_spiciest_foods(spicy_foods):
    pass
    for x in spicy_foods:
       if(x["heat_level"]>5):
            print(f"{x['name']} ({x['cuisine']}) | Heat Level: { '🌶' * x['heat_level']}")

def get_average_heat_level(spicy_foods):
    heat = 0
    pass
    for food in spicy_foods:
        heat = heat + food['heat_level']

    return int(heat/len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
