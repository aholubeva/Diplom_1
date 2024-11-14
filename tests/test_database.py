from praktikum.database import Database
from typing import List
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest



class TestDatabase:

    @pytest.mark.parametrize('bun_name', ["black bun", "white bun", "red bun"])
    def test_available_buns(self, bun_name):
        db = Database()
        buns: List[Bun] = []
        buns.append(Bun("bun_name", 100))
        buns_list = db.available_buns()

        assert len(buns_list) == 3

    @pytest.mark.parametrize('sauce_name', ["black bun", "white bun", "red bun"])
    def test_available_ingredients(self, sauce_name):
        db = Database()
        ingredients: List[Ingredient] = []
        ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sauce_name", 10))
        ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 20))
        ingredient_list = db.available_ingredients()

        assert len(ingredient_list) == 6