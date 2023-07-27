import csv

from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data_reader(source_path)

    def data_reader(self, source_path):
        with open(source_path, newline="") as cvs_file:
            pratos = dict()
            reader = csv.DictReader(cvs_file)
            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                dish_ingredient = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])
                prato = pratos.get(dish_name)
                if not prato:
                    prato = Dish(dish_name, dish_price)
                    pratos[dish_name] = prato
                    self.dishes.add(prato)
                ingrediente = Ingredient(dish_ingredient)
                prato.add_ingredient_dependency(ingrediente, recipe_amount)
