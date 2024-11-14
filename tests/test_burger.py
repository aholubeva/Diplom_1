from praktikum.burger import Burger
from praktikum.bun import Bun
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

    def test_get_price(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200))
        price = burger.get_price()

        assert price == 450

    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(Bun("white bun", 200))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 300))
        receipt = burger.get_receipt()

        assert receipt == '(==== white bun ====)\n= sauce sour cream =\n= filling dinosaur =\n(==== white bun ====)\n\nPrice: 800'



