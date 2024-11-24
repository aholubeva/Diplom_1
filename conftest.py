from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.name = 'булка'
    mock.price = 200
    mock.get_name.return_value = 'булка'
    mock.get_price.return_value = 200
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.name = "hot sauce"
    mock.price = 100
    mock.type = INGREDIENT_TYPE_SAUCE
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock
