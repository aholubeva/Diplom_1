from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient("sauce", "chili", 10)
        price = ingredient.get_price()
        assert price == 10

    def test_get_name(self):
        ingredient = Ingredient("sauce", "chili", 10)
        name = ingredient.get_name()
        assert name == "chili"

    def test_get_type(self):
        ingredient = Ingredient("sauce", "chili", 10)
        ing_type = ingredient.get_type()
        assert ing_type == "sauce"
