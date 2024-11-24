from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)

        assert  ingredient in burger.ingredients


    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert  ingredient not in burger.ingredients and len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 20)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.get_price()

        assert price == 500

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        assert receipt == '(==== булка ====)\n= sauce hot sauce =\n(==== булка ====)\n\nPrice: 500'

