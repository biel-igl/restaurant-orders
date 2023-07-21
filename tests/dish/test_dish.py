from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("pão com ovo", "5.50")
    with pytest.raises(ValueError):
        Dish("pão com ovo", -5)
    prato = Dish("pão com ovo", 5.50)
    assert prato.name == "pão com ovo"
    assert prato.recipe == {}
    assert prato == Dish("pão com ovo", 5.50)
    assert prato.__repr__() == "Dish('pão com ovo', R$5.50)"
    assert prato.__hash__() == prato.__hash__()
    assert prato.__hash__() != hash(Dish("pão com ovo", 5.60))
    ingrediente = Ingredient('ovo')
    prato.add_ingredient_dependency(ingrediente, 2)
    assert prato.recipe == {ingrediente: 2}
    assert prato.get_restrictions()
    assert prato.get_ingredients()
